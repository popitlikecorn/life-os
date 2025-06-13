"""
Frontier Detector - Monitors changes at the frontiers of technology, politics, business
Part of the Intel Branch's environmental scanning capabilities
"""
from typing import Dict, List, Any
from datetime import datetime, timedelta
import json
import requests
import os
try:
    from bs4 import BeautifulSoup
except ImportError:
    raise ImportError(
        "BeautifulSoup4 is required. Install it with `pip install beautifulsoup4`"
    )


class FrontierDetector:

    def __init__(self):
        self.frontiers = {
            "tech": TechnologyFrontier(),
            "politics": PoliticalFrontier(),
            "business": BusinessFrontier(),
            "social": SocialFrontier(),
            "economics": EconomicFrontier()
        }
        self.detection_history = []
        self.significance_threshold = float(
            os.getenv("SIGNIFICANCE_THRESHOLD", 0.7))

    def scan_frontiers(self,
                       sources: List[str] = None) -> List[Dict[str, Any]]:
        """Scan specified frontiers and return raw data"""
        sources = sources or ["tech", "business"]
        print(f"🔍 Frontier Detector: Scanning {sources}...")
        report = self.daily_frontier_scan()
        raw_data = []
        for frontier_name in sources:
            if frontier_name in report["frontier_updates"]:
                raw_data.extend(report["frontier_updates"][frontier_name])
        return raw_data

    def daily_frontier_scan(self) -> Dict[str, Any]:
        """Scan all frontiers for updates"""
        print("🔍 Frontier Detector: Scanning all frontiers...")
        frontier_report = {
            "scan_date": datetime.now().date().isoformat(),
            "timestamp": datetime.now().isoformat(),
            "frontier_updates": {},
            "significant_changes": [],
            "asymmetric_implications": [],
            "strategic_recommendations": []
        }
        for frontier_name, frontier in self.frontiers.items():
            try:
                updates = frontier.detect_changes()
                frontier_report["frontier_updates"][frontier_name] = updates
                significant = [
                    update for update in updates if update.get(
                        "significance", 0) > self.significance_threshold
                ]
                frontier_report["significant_changes"].extend(significant)
            except Exception as e:
                frontier_report["frontier_updates"][frontier_name] = [{
                    "description":
                    f"Scan failed: {str(e)}",
                    "significance":
                    0.0
                }]
        frontier_report[
            "asymmetric_implications"] = self._analyze_asymmetric_implications(
                frontier_report["significant_changes"])
        frontier_report[
            "strategic_recommendations"] = self._generate_strategic_recommendations(
                frontier_report["asymmetric_implications"])
        self.detection_history.append(frontier_report)
        print(
            f"✅ Frontier scan complete. {len(frontier_report['significant_changes'])} significant changes detected."
        )
        return frontier_report

    def _analyze_asymmetric_implications(
            self,
            significant_changes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Analyze changes for asymmetric opportunities"""
        implications = []
        for change in significant_changes:
            desc = change.get("description", "").lower()
            if "ai" in desc or "machine learning" in desc:
                implications.append({
                    "type": "skill_arbitrage_opportunity",
                    "description": "AI advancement creating skill premium",
                    "asymmetry_ratio": "10:1",
                    "time_window": "6-18 months",
                    "action_required": "Develop AI expertise"
                })
            if "regulation" in desc or "policy" in desc:
                implications.append({
                    "type":
                    "regulatory_arbitrage",
                    "description":
                    "Regulatory changes creating gaps",
                    "asymmetry_ratio":
                    "3:1",
                    "time_window":
                    "12-24 months",
                    "action_required":
                    "Position for compliance"
                })
        return implications

    def _generate_strategic_recommendations(
            self, implications: List[Dict[str, Any]]) -> List[str]:
        """Generate recommendations from implications"""
        recommendations = []
        for implication in implications:
            if implication["type"] == "skill_arbitrage_opportunity":
                recommendations.extend([
                    "Start AI skill development",
                    "Connect with AI practitioners"
                ])
            if implication["type"] == "regulatory_arbitrage":
                recommendations.extend([
                    "Research regulatory changes",
                    "Build compliance capabilities"
                ])
        return list(set(recommendations))


class TechnologyFrontier:

    def detect_changes(self) -> List[Dict[str, Any]]:
        """Detect changes in technology frontier"""
        try:
            url = os.getenv("FRONTIER_SOURCE", "https://news.ycombinator.com")
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            headlines = [
                item.text for item in soup.find_all("a", class_="titlelink")
            ]
            return [{
                "area": "technology",
                "description": h,
                "significance": 0.8,
                "impact_timeline": "6-12 months",
                "implications": ["Tech trend shift"]
            } for h in headlines[:2]]
        except Exception as e:
            return [{
                "area": "technology",
                "description": f"Scan failed: {str(e)}",
                "significance": 0.0,
                "impact_timeline": "N/A",
                "implications": []
            }]


class PoliticalFrontier:

    def detect_changes(self) -> List[Dict[str, Any]]:
        """Detect changes in political frontier"""
        try:
            url = os.getenv("FRONTIER_SOURCE", "https://news.ycombinator.com")
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            headlines = [
                item.text for item in soup.find_all("a", class_="titlelink")
            ]
            return [{
                "area": "politics",
                "description": h,
                "significance": 0.7,
                "impact_timeline": "12-24 months",
                "implications": ["Policy shift"]
            } for h in headlines[:2]]
        except Exception as e:
            return [{
                "area": "politics",
                "description": f"Scan failed: {str(e)}",
                "significance": 0.0,
                "impact_timeline": "N/A",
                "implications": []
            }]


class BusinessFrontier:

    def detect_changes(self) -> List[Dict[str, Any]]:
        """Detect changes in business frontier"""
        try:
            url = os.getenv("FRONTIER_SOURCE", "https://news.ycombinator.com")
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            headlines = [
                item.text for item in soup.find_all("a", class_="titlelink")
            ]
            return [{
                "area": "business",
                "description": h,
                "significance": 0.7,
                "impact_timeline": "6-18 months",
                "implications": ["Market shift"]
            } for h in headlines[:2]]
        except Exception as e:
            return [{
                "area": "business",
                "description": f"Scan failed: {str(e)}",
                "significance": 0.0,
                "impact_timeline": "N/A",
                "implications": []
            }]


class SocialFrontier:

    def detect_changes(self) -> List[Dict[str, Any]]:
        """Detect changes in social frontier"""
        try:
            url = os.getenv("FRONTIER_SOURCE", "https://news.ycombinator.com")
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            headlines = [
                item.text for item in soup.find_all("a", class_="titlelink")
            ]
            return [{
                "area": "social",
                "description": h,
                "significance": 0.7,
                "impact_timeline": "ongoing",
                "implications": ["Social trend"]
            } for h in headlines[:2]]
        except Exception as e:
            return [{
                "area": "social",
                "description": f"Scan failed: {str(e)}",
                "significance": 0.0,
                "impact_timeline": "N/A",
                "implications": []
            }]


class EconomicFrontier:

    def detect_changes(self) -> List[Dict[str, Any]]:
        """Detect changes in economic frontier"""
        try:
            url = os.getenv("FRONTIER_SOURCE", "https://news.ycombinator.com")
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            headlines = [
                item.text for item in soup.find_all("a", class_="titlelink")
            ]
            return [{
                "area": "economics",
                "description": h,
                "significance": 0.7,
                "impact_timeline": "6-18 months",
                "implications": ["Economic shift"]
            } for h in headlines[:2]]
        except Exception as e:
            return [{
                "area": "economics",
                "description": f"Scan failed: {str(e)}",
                "significance": 0.0,
                "impact_timeline": "N/A",
                "implications": []
            }]
