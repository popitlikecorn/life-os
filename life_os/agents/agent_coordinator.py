
"""
Agent Coordinator - Manages agent interactions and workflows
"""

from typing import Dict, Any, List
from .agent_factory import AgentFactory, CustomAgent

class AgentCoordinator:
    """
    Coordinates multiple agents working together
    """
    
    def __init__(self):
        self.factory = AgentFactory()
        self.active_workflows = {}
        self.agent_networks = {}
    
    def setup_default_agents(self):
        """Set up the default Life OS agent network"""
        print("🏗️ Setting up default agent network...")
        
        # Create core agents
        intel_scout = self.factory.create_intel_scout()
        strategic_planner = self.factory.create_planning_agent("Strategic Planner", "life_optimization")
        research_agent = self.factory.create_research_agent("Research Specialist", "opportunities")
        
        # Connect agents
        self.factory.connect_agents("Intel Scout", "Strategic Planner", "intel_feed")
        self.factory.connect_agents("Research Specialist", "Intel Scout", "data_support")
        self.factory.connect_agents("Strategic Planner", "Research Specialist", "validation")
        
        print("✅ Default agent network established")
        
        return {
            "intel_scout": intel_scout,
            "strategic_planner": strategic_planner,
            "research_agent": research_agent
        }
    
    def create_custom_agent(self, agent_config: Dict[str, Any]) -> CustomAgent:
        """Create a custom agent from configuration"""
        return self.factory.create_agent(
            name=agent_config["name"],
            role=agent_config["role"],
            instructions=agent_config["instructions"],
            capabilities=agent_config.get("capabilities", [])
        )
    
    def process_multi_agent_query(self, query: str, agent_names: List[str] = None) -> Dict[str, str]:
        """Process a query using multiple agents"""
        if not agent_names:
            agent_names = self.factory.list_agents()
        
        responses = {}
        
        for agent_name in agent_names:
            agent = self.factory.get_agent(agent_name)
            if agent:
                responses[agent_name] = agent.process_query(query)
        
        return responses
    
    def run_agent_workflow(self, workflow_name: str, initial_query: str) -> Dict[str, Any]:
        """Run a predefined agent workflow"""
        if workflow_name == "intel_to_strategy":
            return self._intel_to_strategy_workflow(initial_query)
        elif workflow_name == "research_deep_dive":
            return self._research_deep_dive_workflow(initial_query)
        else:
            print(f"Unknown workflow: {workflow_name}")
            return {}
    
    def _intel_to_strategy_workflow(self, query: str) -> Dict[str, Any]:
        """Intel gathering → Strategic planning workflow"""
        print("🔄 Running Intel → Strategy workflow...")
        
        # Step 1: Intel gathering
        intel_agent = self.factory.get_agent("Intel Scout")
        intel_report = intel_agent.process_query(query) if intel_agent else "No intel agent available"
        
        # Step 2: Strategic planning based on intel
        strategy_agent = self.factory.get_agent("Strategic Planner")
        strategy_plan = strategy_agent.process_query(
            f"Based on this intel: {intel_report}, create a strategic plan for: {query}"
        ) if strategy_agent else "No strategy agent available"
        
        return {
            "workflow": "intel_to_strategy",
            "intel_report": intel_report,
            "strategy_plan": strategy_plan,
            "status": "completed"
        }
    
    def _research_deep_dive_workflow(self, query: str) -> Dict[str, Any]:
        """Research deep dive workflow"""
        print("🔬 Running Research Deep Dive workflow...")
        
        research_agent = self.factory.get_agent("Research Specialist")
        research_report = research_agent.process_query(query) if research_agent else "No research agent available"
        
        return {
            "workflow": "research_deep_dive",
            "research_report": research_report,
            "status": "completed"
        }
