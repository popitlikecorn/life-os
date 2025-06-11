
"""
Protocol Engine - Enforces protocol execution with dependencies and gates
"""

from typing import Dict, Any, List, Optional
from enum import Enum
from datetime import datetime
import json

class ProtocolStatus(Enum):
    NOT_STARTED = "not_started"
    GO_CHECK = "go_check"
    NO_GO = "no_go"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"

class DependencyType(Enum):
    PATH = "path"  # A must complete before B
    CIRCULAR = "circular"  # A and B reinforce each other
    SCALE = "scale"  # Different approach based on scale

class Protocol:
    """A protocol with go/no-go gates and dependencies"""
    
    def __init__(self, name: str, steps: List[str], go_no_go_criteria: Dict[str, Any]):
        self.name = name
        self.steps = steps
        self.go_no_go_criteria = go_no_go_criteria
        self.status = ProtocolStatus.NOT_STARTED
        self.dependencies = []
        self.current_step = 0
        self.execution_log = []
        self.metadata = {}
        
    def add_dependency(self, protocol_name: str, dep_type: DependencyType):
        """Add protocol dependency"""
        self.dependencies.append({
            "protocol": protocol_name,
            "type": dep_type,
            "satisfied": False
        })
        
    def check_go_no_go(self, context: Dict[str, Any]) -> tuple[bool, str]:
        """Check if protocol can proceed"""
        for criterion, requirement in self.go_no_go_criteria.items():
            if criterion == "requires_planning" and not context.get("planning_completed"):
                return False, "No planning completed - NO GO"
            elif criterion == "requires_preparation" and not context.get("preparation_completed"):
                return False, "No preparation completed - NO GO"
            elif criterion == "requires_intel" and not context.get("intel_available"):
                return False, "No intel available - NO GO"
            elif criterion == "requires_edge_hedge_leverage":
                edge = context.get("edge_identified", False)
                hedge = context.get("hedge_in_place", False)
                leverage = context.get("leverage_calculated", False)
                if not all([edge, hedge, leverage]):
                    return False, f"Missing: Edge({edge}), Hedge({hedge}), Leverage({leverage}) - NO GO"
                    
        return True, "All criteria met - GO"
        
    def execute_step(self, step_index: int, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute specific protocol step"""
        if step_index >= len(self.steps):
            return {"status": "completed", "message": "Protocol completed"}
            
        step = self.steps[step_index]
        
        # Log execution
        self.execution_log.append({
            "step": step_index,
            "step_name": step,
            "timestamp": datetime.now().isoformat(),
            "context": context
        })
        
        return {
            "status": "step_completed",
            "step": step,
            "next_step": step_index + 1 if step_index + 1 < len(self.steps) else None
        }

class ProtocolEngine:
    """Manages protocol execution with dependency resolution"""
    
    def __init__(self):
        self.protocols: Dict[str, Protocol] = {}
        self.execution_queue = []
        self.active_executions = {}
        self._initialize_core_protocols()
        
    def register_protocol(self, protocol: Protocol):
        """Register new protocol"""
        self.protocols[protocol.name] = protocol
        
    def execute_protocol(self, protocol_name: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute protocol with full dependency checking"""
        if protocol_name not in self.protocols:
            return {"status": "error", "message": f"Protocol {protocol_name} not found"}
            
        protocol = self.protocols[protocol_name]
        
        # Check dependencies first
        dep_check = self._check_dependencies(protocol, context)
        if not dep_check["satisfied"]:
            return {
                "status": "dependency_failure",
                "message": dep_check["message"],
                "required_protocols": dep_check["required"]
            }
            
        # Check go/no-go criteria
        can_proceed, reason = protocol.check_go_no_go(context)
        if not can_proceed:
            return {
                "status": "no_go",
                "message": reason,
                "suggestions": self._get_no_go_suggestions(protocol, context)
            }
            
        # Execute protocol
        protocol.status = ProtocolStatus.IN_PROGRESS
        execution_result = self._execute_protocol_steps(protocol, context)
        
        if execution_result["status"] == "completed":
            protocol.status = ProtocolStatus.COMPLETED
            
        return execution_result
        
    def get_optimal_workflow(self, goal: str, context: Dict[str, Any]) -> List[str]:
        """Determine optimal workflow for given goal and context"""
        # This is where the "globally optimal but locally optimal is fine" logic goes
        
        # Basic workflow determination based on goal type
        if "research" in goal.lower():
            return ["intel_gathering", "research_protocol", "analysis_protocol"]
        elif "plan" in goal.lower():
            return ["intel_gathering", "planning_protocol", "preparation_protocol"]
        elif "execute" in goal.lower():
            return ["planning_protocol", "preparation_protocol", "execution_protocol"]
        else:
            # Default comprehensive workflow
            return ["intel_gathering", "planning_protocol", "preparation_protocol", "execution_protocol"]
            
    def _check_dependencies(self, protocol: Protocol, context: Dict[str, Any]) -> Dict[str, Any]:
        """Check if protocol dependencies are satisfied"""
        unsatisfied = []
        
        for dep in protocol.dependencies:
            dep_protocol = self.protocols.get(dep["protocol"])
            if not dep_protocol:
                continue
                
            if dep["type"] == DependencyType.PATH:
                if dep_protocol.status != ProtocolStatus.COMPLETED:
                    unsatisfied.append(dep["protocol"])
                    
        if unsatisfied:
            return {
                "satisfied": False,
                "message": f"Unsatisfied dependencies: {', '.join(unsatisfied)}",
                "required": unsatisfied
            }
            
        return {"satisfied": True, "message": "All dependencies satisfied"}
        
    def _get_no_go_suggestions(self, protocol: Protocol, context: Dict[str, Any]) -> List[str]:
        """Get suggestions for resolving no-go conditions"""
        suggestions = []
        
        if not context.get("planning_completed"):
            suggestions.append("Execute planning protocol first")
        if not context.get("preparation_completed"):
            suggestions.append("Execute preparation protocol first")
        if not context.get("intel_available"):
            suggestions.append("Gather intel before proceeding")
            
        return suggestions
        
    def _execute_protocol_steps(self, protocol: Protocol, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute all protocol steps"""
        results = []
        
        for i, step in enumerate(protocol.steps):
            step_result = protocol.execute_step(i, context)
            results.append(step_result)
            
            if step_result["status"] == "failed":
                return {
                    "status": "failed",
                    "step": i,
                    "message": step_result.get("message", "Step failed"),
                    "results": results
                }
                
        return {
            "status": "completed",
            "message": f"Protocol {protocol.name} completed successfully",
            "results": results
        }
        
    def _initialize_core_protocols(self):
        """Initialize core Life OS protocols"""
        
        # Planning Protocol
        planning = Protocol(
            name="planning_protocol",
            steps=[
                "situation_analysis",
                "goal_definition",
                "option_generation",
                "option_evaluation",
                "strategic_selection",
                "tactical_planning"
            ],
            go_no_go_criteria={
                "requires_intel": True,
                "requires_clear_objective": True
            }
        )
        
        # Preparation Protocol  
        preparation = Protocol(
            name="preparation_protocol",
            steps=[
                "resource_identification",
                "resource_acquisition",
                "skill_development",
                "environment_setup",
                "contingency_planning"
            ],
            go_no_go_criteria={
                "requires_planning": True
            }
        )
        
        # Execution Protocol
        execution = Protocol(
            name="execution_protocol", 
            steps=[
                "pre_execution_check",
                "execution_setup",
                "active_execution",
                "monitoring_adjustment",
                "completion_review"
            ],
            go_no_go_criteria={
                "requires_planning": True,
                "requires_preparation": True,
                "requires_edge_hedge_leverage": True
            }
        )
        
        # Set up dependencies
        preparation.add_dependency("planning_protocol", DependencyType.PATH)
        execution.add_dependency("planning_protocol", DependencyType.PATH)
        execution.add_dependency("preparation_protocol", DependencyType.PATH)
        
        # Register protocols
        self.register_protocol(planning)
        self.register_protocol(preparation) 
        self.register_protocol(execution)
