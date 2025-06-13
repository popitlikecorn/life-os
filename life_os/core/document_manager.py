"""
Document Manager - Handles living documents that evolve with thinking
"""
import json
from datetime import datetime
from typing import Dict, Any, List
from pathlib import Path
from life_os.core.living_document import LivingDocument, ProtocolDocument


class DocumentManager:
    """Manages all living documents in the Life OS"""

    def __init__(self, base_path: str = "life_os"):
        self.base_path = Path(base_path)
        self.documents: Dict[str, LivingDocument] = {}
        self.document_index = {}
        self._load_existing_documents()

    def create_document(self,
                        name: str,
                        doc_type: str,
                        content: str = "",
                        **kwargs) -> LivingDocument:
        """Create new living document"""
        if doc_type == "protocol":
            doc = ProtocolDocument(name,
                                   steps=kwargs.get("steps", []),
                                   go_no_go_criteria=kwargs.get(
                                       "criteria", {}))
            if content:
                doc.content = content
        else:
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
            self.documents[name].evolve(new_content, reasoning=reason)
            self._save_document(self.documents[name])

    def add_to_document(self, name: str, insight: str, source: str = ""):
        """Add insight to existing document"""
        if name in self.documents:
            self.documents[name].evolve(insight, source=source)
            self._save_document(self.documents[name])

    def search_documents(self,
                         query: str,
                         doc_type: str = None) -> List[LivingDocument]:
        """Search documents by content or type"""
        results = []
        for doc in self.documents.values():
            if doc_type and doc.doc_type != doc_type:
                continue
            if query.lower() in doc.content.lower() or query.lower(
            ) in doc.name.lower():
                results.append(doc)
        return results

    def get_documents_by_type(self, doc_type: str) -> List[LivingDocument]:
        """Get all documents of specific type"""
        return [
            doc for doc in self.documents.values() if doc.doc_type == doc_type
        ]

    def list_documents(self) -> List[str]:
        """List all document names"""
        return list(self.documents.keys())

    def _save_document(self, doc: LivingDocument):
        """Save document to appropriate location"""
        type_path = self.base_path / doc.doc_type
        type_path.mkdir(parents=True, exist_ok=True)
        file_path = type_path / f"{doc.name.replace(' ', '_').lower()}.json"
        with open(file_path, 'w') as f:
            json.dump(doc.to_dict(), f, indent=2)

    def _load_existing_documents(self):
        """Load existing documents from filesystem"""
        for doc_type in [
                'protocol', 'heuristic', 'playbook', 'worldview', 'targets'
        ]:
            type_path = self.base_path / doc_type
            if type_path.exists():
                for file_path in type_path.glob('*.json'):
                    try:
                        with open(file_path) as f:
                            data = json.load(f)
                        if data['doc_type'] == "protocol":
                            doc = ProtocolDocument(data['name'],
                                                   steps=data.get('steps', []),
                                                   go_no_go_criteria=data.get(
                                                       'go_no_go_criteria',
                                                       {}))
                            doc.content = data.get('content', '')
                        else:
                            doc = LivingDocument.from_dict(data)
                        doc.version = data.get('version', 1)
                        doc.tags = data.get('tags', [])
                        doc.evolution_history = data.get(
                            'evolution_history', [])
                        self.documents[data['name']] = doc
                    except Exception as e:
                        print(f"Error loading document {file_path}: {e}")

    def close(self):
        """Close any open resources"""
        pass
