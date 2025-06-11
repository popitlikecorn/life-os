
"""
Protocol Engine for Life OS
Handles execution of protocols with go/no-go validation
"""

import yaml
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime
from .go_no_go_checker import GoNoGoChecker

class ProtocolEngine:
    """Manages and executes Life OS protocols"""
    
    def __init__(self):
        self.config_path = Path(__file__).parent.parent / "config"
        self.protocols = self._load_protocols()
        self.heuristics = self._load_heuristics()
        self.playbooks = self._load_playbooks()
        self.go_no_go_checker = GoNoGoChecker()
        
    def _load_protocols(self) -> Dict[str, Any]:
        """Load protocol configurations"""
        try:
            with open(self.config_path / "protocols.yaml", 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            print("⚠️  protocols.yaml not found")
            return {}
    
    def _load_heuristics(self) -> Dict[str, Any]:
        """Load heuristic configurations"""
        try:
            with open(self.config_path / "heuristics.yaml", 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            print("⚠️  heuristics.yaml not found")
            return {}
    
    def _load_playbooks(self) -> Dict[str, Any]:
        """Load playbook configurations"""
        try:
            with open(self.config_path / "playbooks.yaml", 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            print("⚠️  playbooks.yaml not found")
            return {}
    
    def execute_protocol(self, protocol_name: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Execute a specific protocol with go/no-go validation"""
        if protocol_name not in self.protocols:
            return {"status": "error", "message": f"Protocol {protocol_name} not found"}
        
        protocol = self.protocols[protocol_name]
        print(f"🔄 Executing protocol: {protocol['name']}")
        
        # Go/No-Go validation
        if 'go_no_go_criteria' in protocol:
            go_decision = self.go_no_go_checker.evaluate_protocol(protocol, context or {})
            if not go_decision:
                return {
                    "status": "no_go", 
                    "message": f"Protocol {protocol_name} failed go/no-go validation",
                    "timestamp": datetime.now().isoformat()
                }
        
        # Execute protocol steps
        results = {
            "status": "success",
            "protocol": protocol_name,
            "started_at": datetime.now().isoformat(),
            "steps_completed": [],
            "context": context or {}
        }
        
        if 'steps' in protocol:
            for step_num, step_desc in protocol['steps'].items():
                print(f"  📋 Step {step_num}: {step_desc}")
                results["steps_completed"].append({
                    "step": step_num,
                    "description": step_desc,
                    "completed_at": datetime.now().isoformat()
                })
        
        results["completed_at"] = datetime.now().isoformat()
        return results
    
    def get_heuristic(self, domain: str) -> Dict[str, Any]:
        """Retrieve heuristics for a specific domain"""
        heuristic_key = f"{domain}_heuristics"
        if heuristic_key in self.heuristics:
            return self.heuristics[heuristic_key]
        return {"error": f"Heuristics for {domain} not found"}
    
    def get_playbook(self, playbook_name: str) -> Dict[str, Any]:
        """Retrieve a specific playbook"""
        if playbook_name in self.playbooks:
            return self.playbooks[playbook_name]
        return {"error": f"Playbook {playbook_name} not found"}
    
    def daily_routine(self) -> Dict[str, Any]:
        """Execute daily routine protocols"""
        print("🌅 Starting daily routine execution...")
        
        routine_protocols = [
            "research_protocol",
            "war_gaming_protocol"
        ]
        
        results = {
            "date": datetime.now().date().isoformat(),
            "protocols_executed": [],
            "overall_status": "success"
        }
        
        for protocol_name in routine_protocols:
            if protocol_name in self.protocols:
                result = self.execute_protocol(protocol_name)
                results["protocols_executed"].append(result)
                if result["status"] != "success":
                    results["overall_status"] = "partial_failure"
        
        return results
    
    def trigger_protocol(self, trigger: str, context: Dict[str, Any] = None) -> List[str]:
        """Find protocols that should be triggered by a specific event"""
        triggered_protocols = []
        
        for protocol_name, protocol_config in self.protocols.items():
            if 'trigger_conditions' in protocol_config:
                if trigger in protocol_config['trigger_conditions']:
                    triggered_protocols.append(protocol_name)
        
        return triggered_protocols
    
    def validate_worldview_alignment(self, decision_context: Dict[str, Any]) -> bool:
        """Check if a decision aligns with current worldview and virtue stack"""
        virtue_stack = self.get_playbook("virtue_stack")
        worldview = self.get_playbook("worldview_framework")
        
        # This would contain more sophisticated logic to validate alignment
        # For now, return True if core elements are present
        return bool(virtue_stack and worldview and decision_context)
