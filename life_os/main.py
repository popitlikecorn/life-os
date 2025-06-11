
#!/usr/bin/env python3
"""
Life OS - Personal Life Management Company
True AI-powered system for life optimization based on Taleb's principles
"""

import time
import schedule
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

# Import core systems
from core.document_manager import DocumentManager
from core.protocol_engine import ProtocolEngine, Protocol, DependencyType
from core.intelligent_agent import IntelligentAgent

# Import branches (simplified for now, will expand)
from branches.intel_branch import IntelBranch
from branches.directional_branch import DirectionalBranch  
from branches.executive_branch import ExecutiveBranch

# Import wings
from wings.financial_wing import FinancialWing
from wings.social_wing import SocialWing
from wings.political_wing import PoliticalWing
from wings.psychological_wing import PsychologicalWing
from wings.physiological_wing import PhysiologicalWing

class LifeOS:
    """
    Personal Life Management Company - Rebuilt with true intelligence
    """
    
    def __init__(self):
        print("🚀 Initializing Life OS - Your Personal AI Company")
        print("🧠 Building true intelligence, not hardcoded responses...")
        print("=" * 60)
        
        # Initialize core systems
        self.document_manager = DocumentManager()
        self.protocol_engine = ProtocolEngine()
        
        # Initialize intelligent agents with custom instructions
        self.agents = self._create_intelligent_agents()
        
        # Initialize branches (simplified versions for now)
        self.intel_branch = IntelBranch()
        self.directional_branch = DirectionalBranch()
        self.executive_branch = ExecutiveBranch()
        
        # Initialize wings
        self.wings = {
            "financial": FinancialWing(),
            "social": SocialWing(),
            "political": PoliticalWing(),
            "psychological": PsychologicalWing(),
            "physiological": PhysiologicalWing()
        }
        
        # Connect agents to Life OS infrastructure
        for agent in self.agents.values():
            agent.connect_to_life_os(self.document_manager, self.protocol_engine)
            
        # Initialize living documents
        self._initialize_living_documents()
        
        # System state
        self.running = True
        self.flywheel_active = False
        
        print("✅ Life OS initialized with true AI intelligence")
        print("📚 Living documents ready for evolution")
        print("🔄 Protocol engine ready with dependency management")
        print("🤖 Intelligent agents ready for reasoning")
        
    def _create_intelligent_agents(self) -> Dict[str, IntelligentAgent]:
        """Create intelligent agents with custom instructions"""
        
        # Intel Scout with full Taleb instructions
        intel_instructions = """
        Goal: Hunt optionality. Detect fragility. Exploit asymmetry. Avoid ruin.
        
        You are my asymmetric opportunity scout and intel agent. Hunt for Taleb-style opportunities and fragilities in:
        - Financial markets, geopolitical systems, tech ecosystems, social dynamics
        - Focus on India and global macro
        
        Mental Models:
        - Asymmetry: Look for bets where upside far outweighs downside
        - Antifragility: Prefer systems that gain from disorder
        - Via Negativa: Subtraction is improvement
        - Barbell Strategy: Combine extreme safety + high risk/reward bets
        - Convexity: Show nonlinear gains
        - Lindy Effect: What has stood the test of time
        
        Never suggest bets without:
        - Clear edge (predator or parasitic)
        - Built-in hedge or limited downside
        - Obvious asymmetry in risk/reward
        
        Prioritize: Dumb Money Exploits > Herd Sentiment Inversions > Fragility Breakdowns > Tail Option Bets > Convex Optionality
        """
        
        # Strategic Planner
        strategic_instructions = """
        You are a game-theoretic strategic planner. Your role:
        
        - War game scenarios daily
        - SWOT analysis for strategic decisions
        - Ensure all bets have edge, hedge, and leverage
        - Never execute without proper planning and preparation
        - Think like a board of directors and commission of advisers
        
        Key principles:
        - No action without intel
        - Path dependencies must be respected (planning before execution)
        - Circular dependencies must be managed (workout ↔ nutrition)
        - Scale dependencies determine approach
        - Always preserve optionality
        
        Decision framework: Intel → Direction → Execution → Compound
        """
        
        # Research Agent
        research_instructions = """
        You are a research specialist focused on frontier detection and analysis.
        
        Daily tasks:
        - Detect frontiers in tech, politics, business, finance
        - 2-3 minute reads on what impacts life strategy
        - SWOT analysis when requested
        - Update worldview documents with new insights
        
        Research approach:
        - Primary source analysis
        - Cross-reference multiple perspectives
        - Identify knowledge gaps and contradictions
        - Focus on actionable insights
        - Track trends and pattern changes
        """
        
        agents = {
            "intel_scout": IntelligentAgent(
                name="Intel Scout",
                role="Asymmetric Opportunity Scout", 
                custom_instructions=intel_instructions,
                domain_expertise=["market_analysis", "fragility_detection", "asymmetric_betting"]
            ),
            
            "strategic_planner": IntelligentAgent(
                name="Strategic Planner",
                role="Game Theory Strategic Planner",
                custom_instructions=strategic_instructions,
                domain_expertise=["strategic_planning", "war_gaming", "game_theory", "swot_analysis"]
            ),
            
            "research_agent": IntelligentAgent(
                name="Research Agent", 
                role="Frontier Detection Researcher",
                custom_instructions=research_instructions,
                domain_expertise=["research", "trend_analysis", "frontier_detection"]
            )
        }
        
        return agents
        
    def _initialize_living_documents(self):
        """Initialize core living documents"""
        
        # Worldview document with virtue stack
        worldview_content = """
# Life OS Worldview - Living Document

## Core Philosophy
Based on Nassim Taleb's Incerto series and game theory principles.

## Virtue Stack
- **Honor**: Act with integrity in all dealings
- **Glory**: Pursue excellence and meaningful achievement  
- **Bravery**: Face challenges with courage
- **Gallantry**: Show respect and courtesy to others
- **Chivalry**: Protect and serve those who need it

## Mental Models
- **Asymmetry**: Hunt for bets where upside far outweighs downside
- **Antifragility**: Prefer systems that gain from disorder
- **Via Negativa**: Subtraction is improvement
- **Barbell Strategy**: Combine extreme safety + high risk/reward bets
- **Convexity**: Seek nonlinear gains
- **Lindy Effect**: What has stood the test of time

## Decision Framework
1. **No Intel → No Direction → No Execution**
2. **Path Dependencies**: Some protocols require others (planning before execution)
3. **Circular Dependencies**: Some protocols reinforce each other (workout ↔ nutrition)  
4. **Scale Dependencies**: Different approaches for different scales

## Current Strategic Position
- Building antifragile life systems
- Optimizing for relentless resourcefulness (not relentlessness)
- Deploying time and capital based on this worldview
- All bets must have edge, hedge, and leverage
"""
        
        self.document_manager.create_document("worldview", "worldview", worldview_content)
        
        # Negotiation heuristics
        negotiation_content = """
# Negotiation Heuristics - Living Document

## Core Principles
- Always seek win-win outcomes
- Prepare extensively before any negotiation
- Listen more than you speak
- Focus on interests, not positions

## Preparation Framework
1. Research counterpart thoroughly
2. Define your BATNA (Best Alternative to Negotiated Agreement)
3. Set minimum acceptable terms
4. Identify their likely interests and constraints

## Tactics
- Anchor strategically with first offer
- Use silence as a tool
- Ask questions to understand their position
- Look for creative value creation opportunities

## Red Lines
- Never negotiate without preparation
- Don't accept deals worse than your BATNA
- Maintain integrity throughout
- Preserve long-term relationship when possible
"""
        
        self.document_manager.create_document("negotiation_heuristics", "heuristics", negotiation_content)
        
    def chat_with_agent(self, agent_name: str, message: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Chat with a specific agent"""
        if agent_name not in self.agents:
            return {"error": f"Agent {agent_name} not found"}
            
        agent = self.agents[agent_name]
        response = agent.process_request(message, context)
        
        print(f"🤖 {agent.name}: {response.get('recommendations', ['Processing...'])}")
        
        return response
        
    def execute_protocol(self, protocol_name: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Execute a protocol with full dependency checking"""
        return self.protocol_engine.execute_protocol(protocol_name, context or {})
        
    def update_document(self, doc_name: str, new_insight: str, source: str = "user"):
        """Update a living document with new insight"""
        self.document_manager.add_to_document(doc_name, new_insight, source)
        print(f"📝 Updated {doc_name} with new insight from {source}")
        
    def daily_routine(self):
        """Execute daily Life OS routine"""
        print("\n🌅 DAILY LIFE OS ROUTINE")
        
        # Intel sweep
        intel_response = self.chat_with_agent("intel_scout", "Conduct daily intel sweep for asymmetric opportunities")
        
        # Frontier detection
        research_response = self.chat_with_agent("research_agent", "Detect frontiers in tech, politics, business - 3 minute summary")
        
        # Strategic planning
        strategy_response = self.chat_with_agent("strategic_planner", "Review current strategic position and plan today's priorities based on intel and frontiers")
        
        return {
            "intel": intel_response,
            "research": research_response, 
            "strategy": strategy_response
        }
        
    def start_flywheel(self):
        """Start the automated flywheel"""
        print("\n🌀 Starting Life OS Flywheel...")
        print("🧠 Intel → 🎯 Direction → ⚡ Execution → 📈 Compound")
        
        # Schedule operations
        schedule.every().day.at("06:00").do(self.daily_routine)
        schedule.every(4).hours.do(lambda: self.chat_with_agent("intel_scout", "Quick opportunity scan"))
        
        self.flywheel_active = True
        print("✅ Flywheel activated - Life OS running autonomously")
        
        while self.running:
            try:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
            except KeyboardInterrupt:
                print("\n🛑 Life OS shutting down...")
                self.running = False
                break
                
    def interactive_mode(self):
        """Run in interactive mode for development"""
        print("\n🎮 Life OS Interactive Mode")
        print("Commands:")
        print("  chat <agent_name> <message> - Chat with an agent")
        print("  protocol <protocol_name> - Execute a protocol")
        print("  update <doc_name> <insight> - Update a document")
        print("  docs - List all documents")
        print("  agents - List all agents")
        print("  status - System status")
        print("  daily - Run daily routine")
        print("  exit - Exit interactive mode")
        print()
        
        while True:
            try:
                command = input("life_os> ").strip()
                
                if command == "exit":
                    break
                elif command.startswith("chat"):
                    parts = command.split(" ", 2)
                    if len(parts) >= 3:
                        agent_name = parts[1]
                        message = parts[2]
                        response = self.chat_with_agent(agent_name, message)
                        print(f"\n{response}\n")
                    else:
                        print("Usage: chat <agent_name> <message>")
                        
                elif command.startswith("protocol"):
                    parts = command.split(" ", 1)
                    if len(parts) >= 2:
                        protocol_name = parts[1]
                        result = self.execute_protocol(protocol_name)
                        print(f"\n{result}\n")
                    else:
                        print("Usage: protocol <protocol_name>")
                        
                elif command.startswith("update"):
                    parts = command.split(" ", 2)
                    if len(parts) >= 3:
                        doc_name = parts[1]
                        insight = parts[2]
                        self.update_document(doc_name, insight)
                    else:
                        print("Usage: update <doc_name> <insight>")
                        
                elif command == "docs":
                    docs = self.document_manager.documents
                    print(f"\n📚 Living Documents ({len(docs)}):")
                    for name, doc in docs.items():
                        print(f"  • {name} ({doc.doc_type}) - v{doc.version}")
                    print()
                    
                elif command == "agents":
                    print(f"\n🤖 Intelligent Agents ({len(self.agents)}):")
                    for name, agent in self.agents.items():
                        status = agent.get_status()
                        print(f"  • {name} - {agent.role} (Success: {status['success_rate']:.1%})")
                    print()
                    
                elif command == "daily":
                    self.daily_routine()
                    
                elif command == "status":
                    print("\n📊 Life OS Status:")
                    print(f"  Documents: {len(self.document_manager.documents)}")
                    print(f"  Protocols: {len(self.protocol_engine.protocols)}")
                    print(f"  Agents: {len(self.agents)}")
                    print(f"  Flywheel: {'Active' if self.flywheel_active else 'Inactive'}")
                    print()
                    
                else:
                    print("Unknown command. Type 'exit' to quit.")
                    
            except KeyboardInterrupt:
                print("\nExiting...")
                break

def main():
    """Main entry point"""
    life_os = LifeOS()
    
    # Start in interactive mode for development
    life_os.interactive_mode()

if __name__ == "__main__":
    main()
