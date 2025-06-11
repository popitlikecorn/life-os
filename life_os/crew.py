
"""
Life OS Crew Management
Handles the coordination of AI agents for life optimization
"""

try:
    import yaml
except ImportError:
    print("⚠️ PyYAML not installed. Please install with: pip install pyyaml")
    yaml = None

from pathlib import Path
from tools.go_no_go_checker import GoNoGoChecker

class Agent:
    """Base Agent class for Life OS"""
    
    def __init__(self, role, backstory, capabilities=None, tools=None, personality=None):
        self.role = role
        self.backstory = backstory
        self.capabilities = capabilities or []
        self.tools = tools or []
        self.personality = personality or []
        self.active = True
        
    def __repr__(self):
        return f"Agent(role='{self.role}')"
    
    def execute_task(self, task_config):
        """Execute a task based on the agent's capabilities"""
        print(f"🤖 {self.role} executing task: {task_config.get('name', 'Unknown')}")
        return True

class LifeOSCrew:
    """Main crew orchestrator for Life OS"""
    
    def __init__(self):
        self.config_path = Path(__file__).parent / "config"
        self.agents_config = self._load_config("agents.yaml")
        self.tasks_config = self._load_config("tasks.yaml")
        self.go_no_go_checker = GoNoGoChecker()
        
        # Initialize strategic agents
        self.intel_scout = Agent(
            role="Intel Scout",
            backstory="Expert in gathering and analyzing environmental intelligence, market trends, and opportunity assessment",
            capabilities=[
                "market_analysis",
                "trend_identification", 
                "opportunity_assessment",
                "competitive_intelligence",
                "risk_scanning"
            ],
            tools=[
                "web_scraper",
                "data_analyzer", 
                "trend_monitor",
                "news_aggregator"
            ],
            personality=[
                "analytical",
                "detail_oriented",
                "proactive",
                "strategic"
            ]
        )
        
        self.game_theorist = Agent(
            role="Strategic Planner",
            backstory="Master of game theory and strategic decision-making with expertise in multi-agent interactions and optimal strategy selection",
            capabilities=[
                "game_theory_analysis",
                "strategic_modeling",
                "decision_optimization",
                "scenario_planning",
                "multi_agent_coordination"
            ],
            tools=[
                "strategy_simulator",
                "decision_tree_builder",
                "payoff_calculator",
                "scenario_generator"
            ],
            personality=[
                "logical",
                "systematic",
                "forward_thinking",
                "strategic"
            ]
        )
        
        self.ops_planner = Agent(
            role="Ops Coordinator",
            backstory="Specialist in operational planning and execution with deep understanding of resource allocation and workflow optimization",
            capabilities=[
                "resource_allocation",
                "workflow_optimization",
                "capacity_planning",
                "execution_coordination",
                "performance_monitoring"
            ],
            tools=[
                "resource_planner",
                "workflow_manager",
                "capacity_analyzer",
                "performance_tracker"
            ],
            personality=[
                "efficient",
                "practical",
                "results_focused",
                "organized"
            ]
        )
        
    def _load_config(self, filename):
        """Load configuration from YAML file"""
        if yaml is None:
            print(f"⚠️ Cannot load {filename} - PyYAML not available")
            return {}
            
        config_file = self.config_path / filename
        try:
            with open(config_file, 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            print(f"⚠️  Configuration file {filename} not found")
            return {}
        except yaml.YAMLError as e:
            print(f"❌ Error parsing {filename}: {e}")
            return {}
    
    def initialize_agents(self):
        """Initialize all AI agents based on configuration"""
        print("🤖 Initializing AI agents...")
        
        # Initialize strategic agents
        print(f"  ✅ Initialized {self.intel_scout.role}")
        print(f"  ✅ Initialized {self.game_theorist.role}")
        print(f"  ✅ Initialized {self.ops_planner.role}")
        
        # Initialize configured agents
        if not self.agents_config:
            print("⚠️  No agent configuration found")
            return
            
        for agent_name, agent_config in self.agents_config.items():
            print(f"  ✅ Initialized {agent_name}")
            
    def execute_tasks(self):
        """Execute tasks using the configured agents"""
        print("\n📋 Starting task execution...")
        
        if not self.tasks_config:
            print("⚠️  No task configuration found")
            return
            
        for task_name, task_config in self.tasks_config.items():
            print(f"  🔄 Processing: {task_name}")
            
            # Use go/no-go checker for task validation
            if self.go_no_go_checker.evaluate_task(task_config):
                print(f"    ✅ Task approved: {task_name}")
            else:
                print(f"    ❌ Task rejected: {task_name}")
    
    def coordinate_strategy(self):
        """Coordinate strategic planning using intel scout, game theorist, and ops planner"""
        print("\n🎯 Starting strategic coordination...")
        
        # Intel gathering phase
        print("📊 Intel Scout gathering intelligence...")
        intel_report = {
            "market_trends": "analyzing current trends",
            "opportunities": "identifying strategic opportunities", 
            "risks": "assessing potential risks"
        }
        
        # Strategic planning phase
        print("🧠 Game Theorist developing strategy...")
        strategy_plan = {
            "optimal_moves": "calculating best strategic moves",
            "contingencies": "preparing backup plans",
            "game_scenarios": "modeling different outcomes"
        }
        
        # Operational planning phase
        print("⚙️  Ops Coordinator planning execution...")
        ops_plan = {
            "resource_allocation": "optimizing resource distribution",
            "timeline": "creating execution timeline",
            "milestones": "defining key checkpoints"
        }
        
        return {
            "intel": intel_report,
            "strategy": strategy_plan,
            "operations": ops_plan
        }
    
    def run(self):
        """Main execution method"""
        print("🚀 Starting Life OS crew operations...")
        
        # Initialize agents
        self.initialize_agents()
        
        # Strategic coordination
        strategic_output = self.coordinate_strategy()
        
        # Execute tasks
        self.execute_tasks()
        
        print("\n✨ Life OS crew operations completed!")
