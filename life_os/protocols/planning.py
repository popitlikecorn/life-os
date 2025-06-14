"""
Enhanced Planning Protocol
Implements the antifragile planning process for Life OS
"""
from typing import Dict, Any, List
from life_os.core.living_document import ProtocolDocument


class EnhancedPlanningProtocol:
    """Implements the Enhanced Planning Protocol"""

    def __init__(self, doc_manager):
        self.doc_manager = doc_manager
        self.protocol = doc_manager.get_document("Enhanced Planning Protocol")

    # life_os/protocols/planning.py (partial, update execute)
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the planning protocol"""
        if not self.protocol:
            return {"status": "error", "message": "Protocol not found"}
        result = {"steps_completed": [], "status": "success"}
        steps = getattr(self.protocol, "steps", [])  # Safe access
        for step in steps:
            if not self._execute_step(step, context):
                result["status"] = "blocked"
                break
            result["steps_completed"].append(step)
        self.protocol.log_execution(result["status"] == "success", context)
        self.doc_manager.create_document("Planning Result",
                                         "targets",
                                         content=str(result))
        return result

    def _execute_step(self, step: str, context: Dict[str, Any]) -> bool:
        """Execute a single protocol step"""
        print(f"🔄 Executing step: {step}")
        return True
