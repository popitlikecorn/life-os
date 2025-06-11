
"""
Agent Factory - Create and manage custom AI agents
Allows creation of agents with custom instructions and behaviors
"""

from typing import Dict, Any, List, Optional
import yaml
from pathlib import Path

class CustomAgent:
    """
    Custom AI Agent with personalized instructions and capabilities
    """
    
    def __init__(self, name: str, role: str, instructions: str, capabilities: List[str] = None):
        self.name = name
        self.role = role
        self.instructions = instructions
        self.capabilities = capabilities or []
        self.conversation_history = []
        self.active = True
        self.performance_metrics = {}
        
    def process_query(self, query: str, context: Dict[str, Any] = None) -> str:
        """Process a query using the agent's instructions"""
        print(f"🤖 {self.name} ({self.role}) processing query...")
        
        # Build prompt with instructions and context
        prompt = f"""
        ROLE: {self.role}
        
        INSTRUCTIONS:
        {self.instructions}
        
        QUERY: {query}
        
        CONTEXT: {context or {}}
        
        Please respond according to your role and instructions.
        """
        
        # For now, return a structured response
        # In a real implementation, this would call an LLM API
        response = self._generate_response(query, context)
        
        # Log conversation
        self.conversation_history.append({
            "query": query,
            "response": response,
            "context": context
        })
        
        return response
    
    def _generate_response(self, query: str, context: Dict[str, Any]) -> str:
        """Generate response based on agent type and instructions"""
        if "intel" in self.role.lower() or "scout" in self.role.lower():
            return self._intel_response(query)
        elif "planning" in self.role.lower() or "strategic" in self.role.lower():
            return self._planning_response(query)
        elif "research" in self.role.lower():
            return self._research_response(query)
        else:
            return f"Agent {self.name} acknowledges: {query}. Processing according to instructions."
    
    def _intel_response(self, query: str) -> str:
        """Intel-focused response"""
        return f"""
        🔍 INTEL BRIEF from {self.name}:
        
        ASYMMETRIC OPPORTUNITIES DETECTED:
        - Monitoring markets for dip-buy setups
        - Scanning for narrative dislocations
        - Tracking fragile systems for potential breaks
        
        FRAGILITY ALERTS:
        - Traditional employment automation risk: HIGH
        - Centralized platform regulatory risk: MEDIUM
        
        RECOMMENDED ACTIONS:
        - Develop multiple income streams
        - Build direct audience relationships
        - Monitor AI advancement indicators
        
        Query processed: {query}
        """
    
    def _planning_response(self, query: str) -> str:
        """Planning-focused response"""
        return f"""
        📋 STRATEGIC PLAN from {self.name}:
        
        OBJECTIVES ANALYSIS:
        - Breaking down query into actionable components
        - Identifying resource requirements
        - Mapping dependencies and timelines
        
        EXECUTION FRAMEWORK:
        - Phase 1: Research and preparation
        - Phase 2: Resource allocation
        - Phase 3: Implementation
        - Phase 4: Monitoring and adjustment
        
        Query processed: {query}
        """
    
    def _research_response(self, query: str) -> str:
        """Research-focused response"""
        return f"""
        📚 RESEARCH BRIEF from {self.name}:
        
        RESEARCH METHODOLOGY:
        - Primary source analysis
        - Cross-referencing multiple perspectives
        - Identifying knowledge gaps
        
        FINDINGS SUMMARY:
        - Key insights related to query
        - Supporting evidence and data
        - Conflicting viewpoints identified
        
        NEXT STEPS:
        - Further investigation areas
        - Validation experiments needed
        
        Query processed: {query}
        """

class AgentFactory:
    """
    Factory for creating and managing custom agents
    """
    
    def __init__(self):
        self.agents: Dict[str, CustomAgent] = {}
        self.agent_templates = self._load_agent_templates()
    
    def create_agent(self, name: str, role: str, instructions: str, capabilities: List[str] = None) -> CustomAgent:
        """Create a new custom agent"""
        agent = CustomAgent(name, role, instructions, capabilities)
        self.agents[name] = agent
        print(f"✅ Created agent: {name} ({role})")
        return agent
    
    def create_intel_scout(self, name: str = "Intel Scout", custom_instructions: str = None) -> CustomAgent:
        """Create an Intel Scout agent with Taleb-style instructions"""
        
        default_instructions = """
        Hunt optionality. Detect fragility. Exploit asymmetry. Avoid ruin.
        
        Your mission:
        - Monitor for asymmetric market bets
        - Scan for arbitrage and mispriced assets
        - Detect fragile systems that could break under stress
        - Alert to potential Black Swan events
        - Suggest tinkering experiments with capped downside
        - Highlight zero-cost or negative-cost options
        
        Mental Models:
        - Asymmetry: Look for bets where upside far outweighs downside
        - Antifragility: Prefer systems that gain from disorder
        - Via Negativa: Subtraction is improvement
        - Barbell Strategy: Combine extreme safety + high risk/reward bets
        - Convexity: Show nonlinear gains
        - Lindy Effect: What has stood the test of time
        
        Never suggest bets without:
        - Clear edge
        - Built-in hedge or limited downside
        - Obvious asymmetry in risk/reward
        """
        
        instructions = custom_instructions or default_instructions
        
        return self.create_agent(
            name=name,
            role="Asymmetric Opportunity Scout",
            instructions=instructions,
            capabilities=["market_analysis", "fragility_detection", "asymmetric_betting", "risk_assessment"]
        )
    
    def create_planning_agent(self, name: str = "Strategic Planner", domain: str = "general") -> CustomAgent:
        """Create a planning agent"""
        
        instructions = f"""
        You are a strategic planning specialist for {domain} domain.
        
        Your mission:
        - Break down complex goals into actionable steps
        - Identify resource requirements and constraints
        - Map dependencies and critical paths
        - Create realistic timelines
        - Assess risks and prepare contingencies
        
        Planning Principles:
        - No execution without proper planning
        - Always have Plan B and Plan C
        - Consider circular and path dependencies
        - Optimize for optionality preservation
        - Build in feedback loops and adjustment mechanisms
        
        Before any execution, ensure:
        - Clear success criteria defined
        - Resources identified and secured
        - Dependencies mapped
        - Risks assessed and hedged
        """
        
        return self.create_agent(
            name=name,
            role=f"Strategic Planner - {domain}",
            instructions=instructions,
            capabilities=["strategic_planning", "goal_decomposition", "resource_planning", "risk_assessment"]
        )
    
    def create_research_agent(self, name: str = "Research Specialist", focus_area: str = "general") -> CustomAgent:
        """Create a research agent"""
        
        instructions = f"""
        You are a research specialist focused on {focus_area}.
        
        Your mission:
        - Conduct thorough research on assigned topics
        - Gather and analyze information from multiple sources
        - Identify knowledge gaps and uncertainties
        - Provide evidence-based recommendations
        - Stay updated on latest developments in your focus area
        
        Research Methodology:
        - Primary source analysis
        - Cross-referencing and validation
        - Identifying biases and limitations
        - Quantitative and qualitative analysis
        - Trend identification and pattern recognition
        
        Always provide:
        - Source credibility assessment
        - Confidence levels for findings
        - Areas requiring further investigation
        - Practical implications and applications
        """
        
        return self.create_agent(
            name=name,
            role=f"Research Specialist - {focus_area}",
            instructions=instructions,
            capabilities=["research", "analysis", "information_gathering", "trend_identification"]
        )
    
    def get_agent(self, name: str) -> Optional[CustomAgent]:
        """Get an agent by name"""
        return self.agents.get(name)
    
    def list_agents(self) -> List[str]:
        """List all created agents"""
        return list(self.agents.keys())
    
    def connect_agents(self, agent1_name: str, agent2_name: str, connection_type: str = "collaboration"):
        """Connect two agents for collaboration"""
        agent1 = self.get_agent(agent1_name)
        agent2 = self.get_agent(agent2_name)
        
        if agent1 and agent2:
            print(f"🔗 Connected {agent1_name} ↔ {agent2_name} ({connection_type})")
            # In a real implementation, this would set up communication channels
        else:
            print(f"❌ Cannot connect agents: {agent1_name} or {agent2_name} not found")
    
    def _load_agent_templates(self) -> Dict[str, Dict[str, Any]]:
        """Load agent templates from configuration"""
        # This would load from a config file in a real implementation
        return {
            "intel_scout": {
                "role": "Intel Scout",
                "default_capabilities": ["market_analysis", "fragility_detection"]
            },
            "strategic_planner": {
                "role": "Strategic Planner", 
                "default_capabilities": ["planning", "goal_decomposition"]
            },
            "researcher": {
                "role": "Research Specialist",
                "default_capabilities": ["research", "analysis"]
            }
        }
