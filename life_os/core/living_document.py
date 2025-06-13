"""
Living Documents - Documents that evolve with your thinking
Core foundation for protocols, heuristics, and playbooks
"""
import json
from datetime import datetime
from typing import Dict, Any, List, Optional
from pathlib import Path


class LivingDocument:
    """
    A document that evolves and adapts with your thinking
    Can be protocols, heuristics, playbooks, or any knowledge artifact
    """

    def __init__(self,
                 name: str,
                 doc_type: str,
                 content: str = "",
                 metadata: Dict[str, Any] = None):
        self.name = name
        self.doc_type = doc_type
        self.content = content
        self.metadata = metadata or {}
        self.version = 1
        self.created_at = datetime.now().isoformat()
        self.last_updated = datetime.now().isoformat()
        self.evolution_history = []
        self.tags = []
        self.cross_references = []
        self.effectiveness_score = 0.0
        self.usage_count = 0

    def evolve(self, new_insight: str, source: str = "", reasoning: str = ""):
        """Evolve the document with new insights"""
        evolution_entry = {
            "timestamp": datetime.now().isoformat(),
            "insight": new_insight,
            "source": source,
            "reasoning": reasoning,
            "version_before": self.version,
            "version_after": self.version + 1
        }

        self.content = self._integrate_insight(new_insight, reasoning)
        self.version += 1
        self.last_updated = datetime.now().isoformat()
        self.evolution_history.append(evolution_entry)

        print(
            f"📈 {self.name} evolved to v{self.version}: {new_insight[:50]}...")

    def _integrate_insight(self, insight: str, reasoning: str) -> str:
        """Intelligently integrate new insight into existing content"""
        integration_header = f"\n\n## Evolution Update (v{self.version + 1})\n"
        integration_header += f"**Date**: {datetime.now().strftime('%Y-%m-%d')}\n"
        integration_header += f"**Insight**: {insight}\n"
        if reasoning:
            integration_header += f"**Reasoning**: {reasoning}\n"

        return self.content + integration_header

    def add_cross_reference(self, doc_name: str, relationship: str):
        """Add reference to another document"""
        self.cross_references.append({
            "document": doc_name,
            "relationship": relationship,
            "added_at": datetime.now().isoformat()
        })

    def mark_usage(self, context: str = ""):
        """Mark document as used - tracks effectiveness"""
        self.usage_count += 1
        self.metadata["last_used"] = datetime.now().isoformat()
        if context:
            self.metadata["last_context"] = context

    def get_related_documents(self) -> List[str]:
        """Get list of related document names"""
        return [ref["document"] for ref in self.cross_references]

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for storage"""
        return {
            "name": self.name,
            "doc_type": self.doc_type,
            "content": self.content,
            "metadata": self.metadata,
            "version": self.version,
            "created_at": self.created_at,
            "last_updated": self.last_updated,
            "evolution_history": self.evolution_history,
            "tags": self.tags,
            "cross_references": self.cross_references,
            "effectiveness_score": self.effectiveness_score,
            "usage_count": self.usage_count
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'LivingDocument':
        """Create document from dictionary"""
        doc = cls(data["name"], data["doc_type"], data["content"],
                  data.get("metadata", {}))
        doc.version = data.get("version", 1)
        doc.created_at = data.get("created_at", datetime.now().isoformat())
        doc.last_updated = data.get("last_updated", datetime.now().isoformat())
        doc.evolution_history = data.get("evolution_history", [])
        doc.tags = data.get("tags", [])
        doc.cross_references = data.get("cross_references", [])
        doc.effectiveness_score = data.get("effectiveness_score", 0.0)
        doc.usage_count = data.get("usage_count", 0)
        return doc


class ProtocolDocument(LivingDocument):
    """Specialized living document for protocols with go/no-go gates"""

    def __init__(self, name: str, steps: List[str],
                 go_no_go_criteria: Dict[str, Any]):
        super().__init__(name, "protocol")
        self.steps = steps
        self.go_no_go_criteria = go_no_go_criteria
        self.dependencies = []
        self.success_rate = 0.0
        self.execution_history = []

    def add_dependency(self, protocol_name: str, dependency_type: str):
        """Add protocol dependency"""
        self.dependencies.append({
            "protocol": protocol_name,
            "type": dependency_type,
            "added_at": datetime.now().isoformat()
        })

    def log_execution(self, success: bool, context: Dict[str, Any] = None):
        """Log protocol execution result"""
        execution = {
            "timestamp":
            datetime.now().isoformat(),
            "success":
            success,
            "context":
            context or {},
            "steps_completed":
            len(self.steps) if success else context.get("steps_completed", 0)
        }
        self.execution_history.append(execution)

        total_executions = len(self.execution_history)
        successful_executions = sum(1 for ex in self.execution_history
                                    if ex["success"])
        self.success_rate = successful_executions / total_executions if total_executions > 0 else 0.0


class HeuristicDocument(LivingDocument):
    """Specialized living document for skill-based heuristics"""

    def __init__(self, name: str, skill_domain: str):
        super().__init__(name, "heuristic")
        self.skill_domain = skill_domain
        self.mastery_level = 0.0
        self.practice_sessions = []
        self.outcomes_tracked = []

    def log_practice(self, context: str, outcome: str, effectiveness: float):
        """Log practice session with outcome"""
        session = {
            "timestamp": datetime.now().isoformat(),
            "context": context,
            "outcome": outcome,
            "effectiveness": effectiveness
        }
        self.practice_sessions.append(session)

        if len(self.practice_sessions) >= 5:
            recent_effectiveness = [
                s["effectiveness"] for s in self.practice_sessions[-5:]
            ]
            self.mastery_level = sum(recent_effectiveness) / len(
                recent_effectiveness)


class PlaybookDocument(LivingDocument):
    """Specialized living document for strategic playbooks"""

    def __init__(self, name: str, domain: str):
        super().__init__(name, "playbook")
        self.domain = domain
        self.principles = []
        self.decision_frameworks = []
        self.real_world_applications = []

    def add_principle(self, principle: str, rationale: str = ""):
        """Add new principle to playbook"""
        self.principles.append({
            "principle": principle,
            "rationale": rationale,
            "added_at": datetime.now().isoformat()
        })
        self.evolve(f"Added principle: {principle}", reasoning=rationale)

    def add_decision_framework(self, situation: str, framework: str):
        """Add decision framework for specific situations"""
        self.decision_frameworks.append({
            "situation": situation,
            "framework": framework,
            "added_at": datetime.now().isoformat()
        })
