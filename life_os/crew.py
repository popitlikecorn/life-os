
"""
Life OS Crew Management
Handles the coordination of AI agents for life optimization
"""

import yaml
from pathlib import Path
from tools.go_no_go_checker import GoNoGoChecker

class LifeOSCrew:
    """Main crew orchestrator for Life OS"""
    
    def __init__(self):
        self.config_path = Path(__file__).parent / "config"
        self.agents_config = self._load_config("agents.yaml")
        self.tasks_config = self._load_config("tasks.yaml")
        self.go_no_go_checker = GoNoGoChecker()
        
    def _load_config(self, filename):
        """Load configuration from YAML file"""
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
    
    def run(self):
        """Main execution method"""
        print("🚀 Starting Life OS crew operations...")
        
        # Initialize agents
        self.initialize_agents()
        
        # Execute tasks
        self.execute_tasks()
        
        print("\n✨ Life OS crew operations completed!")
