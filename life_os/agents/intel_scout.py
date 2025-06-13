"""
Intel Scout Agent - Asymmetric Opportunity Detection
Specialized agent for hunting optionality, detecting fragility, and exploiting asymmetry
Based on Taleb's principles from the Incerto series
"""
from typing import Dict, Any, List
from datetime import datetime
import json
import os
from core.intelligent_agent import IntelligentAgent
from core.frontier_detector import FrontierDetector


class IntelScout:
    """
    Asymmetric opportunity scout using IntelligentAgent and FrontierDetector
    """

    def __init__(self):
        self.role = "Intel Scout"
        self.mission = os.getenv(
            "INTEL_SCOUT_MISSION",
            "Hunt optionality. Detect fragility. Exploit asymmetry. Avoid ruin."
        )
        self.focus_areas = [
            "financial_markets", "geopolitical_systems", "tech_ecosystems",
            "social_dynamics", "business_opportunities"
        ]
        self.mental_models = {
            "asymmetry": "Look for bets where upside far outweighs downside",
            "antifragility": "Prefer systems that gain from disorder",
            "via_negativa": "Subtraction is improvement",
            "barbell_strategy":
            "Combine extreme safety + high risk/reward bets",
            "convexity": "Seek nonlinear gains",
            "lindy_effect": "What has stood the test of time"
        }
        self.agent = IntelligentAgent(name="Intel Scout",
                                      role=self.role,
                                      custom_instructions=self.mission,
                                      domain_expertise=self.focus_areas)
        self.frontier_detector = FrontierDetector()
        self.intel_reports = []

    def daily_intel_sweep(self) -> Dict[str, Any]:
        print("🔍 Intel Scout conducting daily sweep...")
        intel_brief = {
            "date": datetime.now().date().isoformat(),
            "timestamp": datetime.now().isoformat(),
            "priority_alerts": [],
            "opportunities": [],
            "fragilities": [],
            "asymmetric_bets": [],
            "frontier_updates": {}
        }
        frontier_report = self.frontier_detector.daily_frontier_scan()
        intel_brief["frontier_updates"] = frontier_report["frontier_updates"]
        context = {
            "frontier_report": frontier_report,
            "mental_models": self.mental_models
        }
        request = "Analyze frontier updates for asymmetric opportunities and fragilities."
        response = self.agent.process_request(request, context)
        intel_brief["opportunities"] = response.get("opportunities_detected",
                                                    [])
        intel_brief["fragilities"] = self._detect_fragilities(response)
        intel_brief["asymmetric_bets"] = self._identify_asymmetric_bets(
            response)
        intel_brief["priority_alerts"] = self._generate_priority_alerts(
            intel_brief)
        self.intel_reports.append(intel_brief)
        return intel_brief

    def generate_briefing(self, topic: str) -> Dict[str, Any]:
        frontier_report = self.frontier_detector.daily_frontier_scan()
        context = {
            "frontier_report": frontier_report,
            "mental_models": self.mental_models
        }
        request = f"Generate a briefing on {topic} using frontier data and Taleb's principles."
        return self.agent.process_request(request, context)

    def _detect_fragilities(self, response: Dict[str,
                                                 Any]) -> List[Dict[str, Any]]:
        fragilities = []
        if "fragility" in response.get("response", "").lower():
            fragilities.append({
                "system": "detected_system",
                "fragility_type": "system_risk",
                "stress_factors": ["external_shocks"],
                "hedge_strategy": "Diversify dependencies",
                "urgency": "medium"
            })
        return fragilities

    def _identify_asymmetric_bets(
            self, response: Dict[str, Any]) -> List[Dict[str, Any]]:
        bets = []
        if "opportunity" in response.get("response", "").lower():
            bets.append({
                "bet_type": "strategic_investment",
                "description": response.get("response", "")[:100],
                "downside": "Minimal",
                "upside": "High",
                "probability": "Medium",
                "time_to_payoff": "6-12 months"
            })
        return bets

    def _generate_priority_alerts(
            self, intel_brief: Dict[str, Any]) -> List[Dict[str, Any]]:
        alerts = []
        for opp in intel_brief["opportunities"]:
            if "10:1" in opp.get("asymmetry_ratio", ""):
                alerts.append({
                    "type": "high_asymmetry_opportunity",
                    "message": f"High asymmetry: {opp['description']}",
                    "urgency": "high",
                    "action": opp.get("action_required", "")
                })
        for frag in intel_brief["fragilities"]:
            if frag.get("urgency") == "high":
                alerts.append({
                    "type": "critical_fragility",
                    "message": f"High fragility: {frag['system']}",
                    "urgency": "high",
                    "action": f"Hedge: {frag['hedge_strategy']}"
                })
        return alerts

    def generate_weekly_intel_summary(self) -> Dict[str, Any]:
        if not self.intel_reports:
            return {"message": "No intel reports available"}
        recent_reports = self.intel_reports[-7:]
        summary = {
            "week_ending": datetime.now().date().isoformat(),
            "reports_analyzed": len(recent_reports),
            "key_trends": self._analyze_trends(recent_reports),
            "top_opportunities": self._rank_opportunities(recent_reports),
            "critical_alerts": self._consolidate_alerts(recent_reports),
            "recommended_actions": []
        }
        summary["recommended_actions"] = self._generate_recommendations(
            summary)
        return summary

    def _analyze_trends(self, reports: List[Dict[str, Any]]) -> List[str]:
        trends = []
        for report in reports:
            for update in report["frontier_updates"].values():
                if "AI" in str(update).lower():
                    trends.append("AI adoption accelerating")
        return list(set(trends))

    def _rank_opportunities(
            self, reports: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        all_op = [
            opp for report in reports
            for opp in report.get("opportunities", [])
        ]
        return sorted(all_op,
                      key=lambda x: x.get("asymmetry_ratio", ""),
                      reverse=True)[:5]

    def _consolidate_alerts(
            self, reports: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        all_alerts = [
            alert for report in reports
            for alert in report.get("priority_alerts", [])
        ]
        unique_alerts = {alert["message"]: alert for alert in all_alerts}
        return sorted(unique_alerts.values(),
                      key=lambda x: x.get("urgency", "low") == "high",
                      reverse=True)

    def _generate_recommendations(self, summary: Dict[str, Any]) -> List[str]:
        recs = []
        for opp in summary["top_opportunities"]:
            if "action_required" in opp:
                recs.append(opp["action_required"])
        return list(set(recs))
