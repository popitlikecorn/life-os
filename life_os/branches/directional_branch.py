"""
Directional Branch - Strategic Direction and Game-Theoretic Planning
Sets optimal strategic direction using game theory, SWOT, and frontier intelligence
Part of the macro flywheel: Intel → Direction → Execution → Compound
"""
from typing import Dict, Any, List
from datetime import datetime
from life_os.core.document_manager import DocumentManager


class DirectionalBranch:
    """
    Strategic Direction Core - The planning hub of LifeOS
    Sets optimal direction using game theory and frontier intelligence
    """

    def __init__(self, document_manager: DocumentManager):
        self.role = "Chief Strategy Officer"
        self.mission = "Optimize strategic direction for antifragile outcomes."
        self.document_manager = document_manager
        self.strategic_plans: List[Dict] = []

    def set_strategic_direction(
            self, intelligence_report: Dict[str, Any]) -> Dict[str, Any]:
        """Generate strategic direction based on intelligence"""
        print("🧭 Directional Branch: Setting strategic course...")
        opportunities = intelligence_report.get("opportunities", [])
        fragilities = intelligence_report.get("fragilities", [])
        tactical_priorities = []
        for opp in opportunities[:3]:
            action = {
                "action": opp["description"],
                "priority": 1 if opp["asymmetry_ratio"] == "100:1" else 2,
                "timeline":
                "30 days" if opp["asymmetry_ratio"] == "100:1" else "90 days",
                "resources_needed": ["time", "network"]
            }
            tactical_priorities.append(action)
        for fragility in fragilities[:2]:
            action = {
                "action": f"Mitigate fragility in {fragility['system']}",
                "priority": 1,
                "timeline": "60 days",
                "resources_needed": ["analysis", "tools"]
            }
            tactical_priorities.append(action)
        strategic_plan = {
            "timestamp":
            datetime.now().isoformat(),
            "tactical_priorities":
            tactical_priorities,
            "strategic_horizon":
            "6 months",
            "swot_analysis":
            self._perform_swot_analysis(intelligence_report),
            "game_theory_outcomes":
            self._simulate_game_theory_scenarios(tactical_priorities)
        }
        self.strategic_plans.append(strategic_plan)
        # Store targets in DocumentManager
        targets_doc = self.document_manager.create_document(
            "Strategic Targets",
            "targets",
            content=json.dumps(tactical_priorities))
        return strategic_plan

    def _perform_swot_analysis(
            self, intelligence_report: Dict[str, Any]) -> Dict[str, List[str]]:
        """Perform SWOT analysis based on intelligence"""
        return {
            "strengths": ["Adaptable systems", "Strong network"],
            "weaknesses": ["Limited deep work time"],
            "opportunities": [
                opp["description"]
                for opp in intelligence_report.get("opportunities", [])
            ],
            "threats": [
                f"Fragility in {frag['system']}"
                for frag in intelligence_report.get("fragilities", [])
            ]
        }

    def _simulate_game_theory_scenarios(
            self, priorities: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Simulate game theory scenarios for priorities"""
        scenarios = []
        for priority in priorities:
            scenarios.append({
                "action":
                priority["action"],
                "payoff_matrix": {
                    "cooperate": {
                        "success": 0.8,
                        "failure": 0.2
                    },
                    "compete": {
                        "success": 0.6,
                        "failure": 0.4
                    }
                },
                "recommended_strategy":
                "cooperate" if priority["priority"] == 1 else "compete"
            })
        return scenarios

    def get_status(self) -> Dict[str, Any]:
        """Return current strategic status with targets"""
        if self.strategic_plans:
            return {
                "active_plans":
                len(self.strategic_plans),
                "last_updated":
                self.strategic_plans[-1]["timestamp"],
                "strategic_targets":
                self.strategic_plans[-1]["tactical_priorities"]
            }
        return {
            "active_plans": 0,
            "last_updated": "Never",
            "strategic_targets": []
        }
