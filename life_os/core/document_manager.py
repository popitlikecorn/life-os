
"""
Document Manager - Handles living documents that evolve with thinking
"""

import os
import json
from datetime import datetime
from typing import Dict, Any, List
from pathlib import Path

class LivingDocument:
    """A document that evolves and updates based on new insights"""
    
    def __init__(self, name: str, doc_type: str, content: str = ""):
        self.name = name
        self.doc_type = doc_type  # protocol, heuristic, playbook, worldview
        self.content = content
        self.version = 1
        self.last_updated = datetime.now()
        self.update_history = []
        self.tags = []
        
    def update_content(self, new_content: str, reason: str = ""):
        """Update document content with version tracking"""
        self.update_history.append({
            "version": self.version,
            "content": self.content,
            "timestamp": self.last_updated.isoformat(),
            "reason": reason
        })
        
        self.content = new_content
        self.version += 1
        self.last_updated = datetime.now()
        
    def add_insight(self, insight: str, source: str = ""):
        """Add new insight to document"""
        insight_block = f"\n\n## Insight ({datetime.now().strftime('%Y-%m-%d')})\n"
        insight_block += f"**Source:** {source}\n" if source else ""
        insight_block += f"{insight}\n"
        
        self.update_content(self.content + insight_block, f"Added insight from {source}")
        
    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "doc_type": self.doc_type,
            "content": self.content,
            "version": self.version,
            "last_updated": self.last_updated.isoformat(),
            "tags": self.tags,
            "update_history": self.update_history
        }

class DocumentManager:
    """Manages all living documents in the Life OS"""
    
    def __init__(self, base_path: str = "life_os"):
        self.base_path = Path(base_path)
        self.documents: Dict[str, LivingDocument] = {}
        self.document_index = {}
        self._load_existing_documents()
        
    def create_document(self, name: str, doc_type: str, content: str = "") -> LivingDocument:
        """Create new living document"""
        doc = LivingDocument(name, doc_type, content)
        self.documents[name] = doc
        self._save_document(doc)
        return doc
        
    def get_document(self, name: str) -> LivingDocument:
        """Get document by name"""
        return self.documents.get(name)
        
    def update_document(self, name: str, new_content: str, reason: str = ""):
        """Update existing document"""
        if name in self.documents:
            self.documents[name].update_content(new_content, reason)
            self._save_document(self.documents[name])
            
    def add_to_document(self, name: str, insight: str, source: str = ""):
        """Add insight to existing document"""
        if name in self.documents:
            self.documents[name].add_insight(insight, source)
            self._save_document(self.documents[name])
            
    def search_documents(self, query: str, doc_type: str = None) -> List[LivingDocument]:
        """Search documents by content or type"""
        results = []
        for doc in self.documents.values():
            if doc_type and doc.doc_type != doc_type:
                continue
            if query.lower() in doc.content.lower() or query.lower() in doc.name.lower():
                results.append(doc)
        return results
        
    def get_documents_by_type(self, doc_type: str) -> List[LivingDocument]:
        """Get all documents of specific type"""
        return [doc for doc in self.documents.values() if doc.doc_type == doc_type]
        
    def _save_document(self, doc: LivingDocument):
        """Save document to appropriate location"""
        type_path = self.base_path / doc.doc_type
        type_path.mkdir(parents=True, exist_ok=True)
        
        file_path = type_path / f"{doc.name.replace(' ', '_').lower()}.json"
        with open(file_path, 'w') as f:
            json.dump(doc.to_dict(), f, indent=2)
            
    def _load_existing_documents(self):
        """Load existing documents from filesystem"""
        for doc_type in ['protocols', 'heuristics', 'playbooks', 'worldview']:
            type_path = self.base_path / doc_type
            if type_path.exists():
                for file_path in type_path.glob('*.json'):
                    try:
                        with open(file_path) as f:
                            data = json.load(f)
                        doc = LivingDocument(data['name'], data['doc_type'], data['content'])
                        doc.version = data.get('version', 1)
                        doc.tags = data.get('tags', [])
                        doc.update_history = data.get('update_history', [])
                        self.documents[data['name']] = doc
                    except Exception as e:
                        print(f"Error loading document {file_path}: {e}")
