"""
Life OS Crew Management
Handles the coordination of AI agents for life optimization
"""
import yaml
from pathlib import Path
from typing import Dict, Any
from life_os.tools.go_no_go_checker import GoNoGoChecker
from life_os.branches.intel_branch import IntelBranch
from life_os.branches.directional_branch import DirectionalBranch
from life_os.branches.executive_branch import ExecutiveBranch
from life_os.core.document_manager import DocumentManager


class Agent:
    """Base Agent class for Life OS"""

    def __init__(self,
                 role,
                 backstory,
                 capabilities=None,
                 tools=None,
                 personality=None):
        self.role = role
        self.backstory = backstory
        self.capabilities = capabilities or []
        self.tools = tools or []
        self.personality = personality or []
        self.active = True

    def __repr__(self):
        return f"Agent(role='{self.role}')"

    def execute_task(self, task_config, context: Dict[str, Any]):
        """Execute a task based on the agent's capabilities"""
        print(
            f"🤖 {self.role} executing task: {task_config.get('name', 'Unknown')}"
        )
        return {
            "status": "completed",
            "result": f"{self.role} completed {task_config.get('name')}"
        }


class LifeOSCrew:
    """Main crew orchestrator for Life OS"""

    def __init__(self, doc_manager: DocumentManager):
        self.config_path = Path(__file__).parent / "config"
        self.agents_config = self._load_config("agents.yaml")
        self.tasks_config = self._load_config("tasks.yaml")
        self.doc_manager = doc_manager
        self.go_no_go_checker = GoNoGoChecker()
        self.intel_branch = IntelBranch(doc_manager)
        self.directional_branch = DirectionalBranch(doc_manager)
        self.executive_branch = ExecutiveBranch(doc_manager)

        self.agents = {
            "intel_scout":
            Agent(
                role="Intel Scout",
                backstory=
                "Expert in gathering and analyzing environmental intelligence",
                capabilities=self.agents_config.get("intel_scout", {}).get(
                    "capabilities", ["technology", "business"]),
                tools=["web_scraper", "data_analyzer"],
                personality=["analytical", "detail_oriented"]),
            "game_theorist":
            Agent(
                role="Strategic Planner",
                backstory=
                "Master of strategy, planning, learning, and financial analysis",
                capabilities=self.agents_config.get("game_theorist", {}).get(
                    "capabilities",
                    ["strategy", "planning", "learning", "financial"]),
                tools=["strategy_simulator", "decision_tree_builder"],
                personality=["logical", "strategic"]),
            "ops_planner":
            Agent(
                role="Ops Coordinator",
                backstory=
                "Specialist in operations, coordination, wellness, and habits",
                capabilities=self.agents_config.get("ops_planner", {}).get(
                    "capabilities",
                    ["operations", "coordination", "wellness", "habit"]),
                tools=["resource_planner", "workflow_manager"],
                personality=["efficient", "organized"])
        }

    def _load_config(self, filename):
        """Load configuration from YAML file"""
        config_file = self.config_path / filename
        try:
            with open(config_file, 'r') as f:
                return yaml.safe_load(f) or {}
        except (FileNotFoundError, yaml.YAMLError) as e:
            print(f"⚠️ Error loading {filename}: {e}")
            return {}

    def initialize_agents(self):
        """Initialize all AI agents"""
        print("🤖 Initializing AI agents...")
        for agent_name, agent in self.agents.items():
            print(f"  ✅ Initialized {agent_name}")

    def execute_tasks(self, context: Dict[str, Any]):
        """Execute tasks using configured agents"""
        print("\n📋 Starting task execution...")
        if not self.tasks_config:
            print("⚠️ No task configuration found")
            return

        for task_name, task_config in self.tasks_config.items():
            print(f"  🔄 Processing: {task_name}")
            if self.go_no_go_checker.evaluate_task(task_config, context):
                agent_name = task_config.get('assigned_agent')
                if agent_name in self.agents:
                    result = self.agents[agent_name].execute_task(
                        task_config, context)
                    print(f"    ✅ Task completed: {result['result']}")
                    self.doc_manager.create_document(
                        f"Task Result: {task_name}",
                        "targets",
                        content=str(result))
                else:
                    print(f"    ❌ No agent assigned for {task_name}")
            else:
                print(f"    ❌ Task rejected: {task_name}")

    def coordinate_strategy(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Coordinate strategic planning across branches"""
        print("\n🎯 Starting strategic coordination...")

        # Intel phase
        print("📊 Intel Scout gathering intelligence...")
        frontier_report = self.intel_branch.scout_frontier()
        self.doc_manager.add_to_document("Worldview Framework",
                                         insight=str(frontier_report),
                                         source="frontier_scan")

        # Strategy phase
        print("🧠 Game Theorist developing strategy...")
        strategy_plan = self.directional_branch.get_status()
        self.doc_manager.create_document("Strategic Plan",
                                         "targets",
                                         content=str(strategy_plan))

        # Operations phase
        print("⚙️ Ops Coordinator planning execution...")
        protocol = self.doc_manager.get_document("Enhanced Planning Protocol")
        if protocol and self.go_no_go_checker.evaluate_protocol(
                protocol, context):
            ops_result = self.executive_branch.run_protocol(
                "Enhanced Planning Protocol", context)
        else:
            ops_result = "Protocol blocked by go/no-go criteria"

        return {
            "intel": frontier_report,
            "strategy": strategy_plan,
            "operations": ops_result
        }

    def run(self, context: Dict[str, Any]):
        """Main execution method"""
        print("🚀 Starting Life OS crew operations...")
        self.initialize_agents()
        strategic_output = self.coordinate_strategy(context)
        self.execute_tasks(context)
        print("\n✨ Life OS crew operations completed!")
        return strategic_output
