"""
Intel Branch - Advanced Intelligence Gathering and Analysis
Frontier detection, opportunity scouting, worldview evolution
Part of the macro flywheel: Intel → Direction → Execution → Compound
"""
import json
import requests
from datetime import datetime
from typing import Dict, List, Any
from life_os.core.frontier_detector import FrontierDetector
from life_os.core.living_document import LivingDocument
from life_os.core.document_manager import DocumentManager


class IntelBranch:
    """
    Intelligence Core - The sensory and analytical hub of LifeOS
    Scans frontiers, identifies opportunities, evolves worldview
    """

    def __init__(self, document_manager: DocumentManager):
        self.role = "Chief Intelligence Officer"
        self.mission = "Detect and analyze opportunities to drive antifragile outcomes."
        self.document_manager = document_manager
        self.frontier_detector = FrontierDetector()
        self.intel_reports: List[Dict] = []
        self.worldview = self.document_manager.get_document(
            "Worldview Framework")

    def gather_intelligence(self, sources: List[str] = None) -> Dict[str, Any]:
        """Collect raw intelligence from specified sources"""
        print("🔎 Intel: Scanning frontiers...")
        raw_data = self.frontier_detector.scan_frontiers(
            sources or ["tech", "markets"])
        return {
            "timestamp": datetime.now().isoformat(),
            "raw_data": raw_data,
            "source_count": len(raw_data)
        }

    def process_intelligence(self, raw_intel: Dict[str,
                                                   Any]) -> Dict[str, Any]:
        """Analyze raw intelligence into actionable insights"""
        print("🧠 Intel: Processing intelligence...")
        opportunities = []
        fragilities = []
        for item in raw_intel.get("raw_data", []):
            if item.get("asymmetry_ratio", "1:1") in ["10:1", "100:1"]:
                opportunities.append({
                    "description":
                    item.get("description", ""),
                    "asymmetry_ratio":
                    item.get("asymmetry_ratio")
                })
            elif item.get("fragility", False):
                fragilities.append({
                    "system":
                    item.get("system", ""),
                    "stress_factors":
                    item.get("stress_factors", [])
                })
        report = {
            "timestamp":
            datetime.now().isoformat(),
            "opportunities":
            opportunities,
            "fragilities":
            fragilities,
            "priority_alerts": [{
                "urgency": "high",
                "item": opp
            } for opp in opportunities if opp["asymmetry_ratio"] == "100:1"]
        }
        self.intel_reports.append(report)
        if self.worldview and hasattr(self.worldview, 'evolve'):
            try:
                self.worldview.evolve(new_insight=json.dumps(report),
                                      source="intelligence_processing")
            except Exception as e:
                print(f"Failed to evolve worldview: {e}")
        return report

    def scout_frontier(self) -> Dict[str, Any]:
        """Scout frontier for opportunities and X interests"""
        raw_intel = self.gather_intelligence(["tech", "markets", "x"])
        report = self.process_intelligence(raw_intel)
        # Placeholder X API call (replace with actual credentials)
        try:
            x_data = requests.get(
                "https://api.x.com/2/tweets/search/recent?query=from:user",
                headers={
                    "Authorization": "Bearer YOUR_X_TOKEN"
                }).json()
            report["x_interests"] = [
                tweet.get("text", "") for tweet in x_data.get("data", [])[:3]
            ]
        except Exception as e:
            report["x_interests"] = f"X API error: {str(e)}"
        return report

    def get_worldview(self) -> Dict[str, Any]:
        """Return current worldview"""
        if self.worldview:
            return {
                "virtues":
                self.worldview.content.split("Virtues: ")[1].split("\n")[0]
                if "Virtues: " in self.worldview.content else "None",
                "version":
                self.worldview.version
            }
        return {"virtues": "None", "version": 0}

    def get_status(self) -> Dict[str, Any]:
        """Return current intelligence status"""
        return {
            "active_reports":
            len(self.intel_reports),
            "last_updated":
            self.intel_reports[-1]["timestamp"]
            if self.intel_reports else "Never",
            "worldview_version":
            self.worldview.version if self.worldview else 0
        }
