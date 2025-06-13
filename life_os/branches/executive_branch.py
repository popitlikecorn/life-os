"""
Executive Branch - Task Execution and Protocol Management
Implements operational protocols and tracks execution
Part of the macro flywheel: Intel → Direction → Execution → Compound
"""
from datetime import datetime
from typing import Dict, Any
from life_os.core.document_manager import DocumentManager
from life_os.tools.go_no_go_checker import GoNoGoChecker
from life_os.protocols.planning import EnhancedPlanningProtocol


class ExecutiveBranch:
    """
    Execution Core - The operational hub of LifeOS
    Manages tasks, executes protocols, and tracks outcomes
    """

    def __init__(self, document_manager: DocumentManager):
        self.role = "Chief Operating Officer"
        self.mission = "Execute protocols and tasks to achieve antifragile outcomes."
        self.document_manager = document_manager
        self.task_queue = []
        self.execution_reports = []
        self.go_no_go_checker = GoNoGoChecker()
        self.protocols = {
            "Enhanced Planning Protocol":
            EnhancedPlanningProtocol(document_manager)
        }

    def run_protocol(self, protocol_name: str, context: Dict[str, Any]) -> str:
        """Execute specified protocol with go/no-go check"""
        print(f"⚙️ Executing protocol: {protocol_name}")
        # Case-insensitive protocol lookup
        protocol = None
        for doc_name in self.document_manager.list_documents():
            if doc_name.lower() == protocol_name.lower():
                protocol = self.document_manager.get_document(doc_name)
                protocol_name = doc_name  # Use exact name for consistency
                break

        if not protocol:
            return f"Error: {protocol_name} is not a valid protocol"

        if self.go_no_go_checker.evaluate_protocol(protocol, context):
            if protocol_name in self.protocols:
                result = self.protocols[protocol_name].execute(context)
                return f"Protocol {protocol_name}: {result['status']}, Steps: {', '.join(result['steps_completed'])}"
            return f"Protocol {protocol_name} executed successfully"
        else:
            return f"Protocol {protocol_name} blocked by go/no-go criteria"

    def schedule_task(self, task: Dict[str, Any]):
        """Add task to execution queue"""
        task["status"] = "pending"
        task["queued_at"] = datetime.now().isoformat()
        self.task_queue.append(task)

    def execute_tasks(self):
        """Execute tasks in queue"""
        completed = []
        for task in self.task_queue:
            if task["status"] == "pending":
                task["status"] = "completed"
                task["completed_at"] = datetime.now().isoformat()
                completed.append(task)
        return completed

    def get_status(self) -> Dict[str, Any]:
        """Return current execution status"""
        return {
            "active_tasks":
            len([t for t in self.task_queue if t["status"] == "pending"]),
            "pending_tasks":
            len(self.task_queue),
            "completed_tasks":
            len([t for t in self.task_queue if t["status"] == "completed"]),
            "execution_reports":
            len(self.execution_reports),
            "last_execution":
            self.execution_reports[-1]["timestamp"]
            if self.execution_reports else "Never"
        }
