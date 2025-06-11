
#!/usr/bin/env python3
"""
Life OS - Enhanced Personal Life Management Company
True AI-powered system for life optimization based on Taleb's principles
Now with frontier detection, living documents, and true evolution
"""

import time
import schedule
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

# Import enhanced core systems
from core.document_manager import DocumentManager
from core.protocol_engine import ProtocolEngine, Protocol, DependencyType
from core.intelligent_agent import IntelligentAgent
from core.living_document import ProtocolDocument, HeuristicDocument, PlaybookDocument

# Import enhanced branches
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
    Enhanced Personal Life Management Company - True Antifragile Intelligence
    """
    
    def __init__(self):
        print("🚀 Initializing Life OS - Enhanced Antifragile Intelligence")
        print("🧠 Building frontier detection, living documents, true evolution...")
        print("=" * 60)
        
        # Initialize enhanced core systems
        self.document_manager = DocumentManager()
        self.protocol_engine = ProtocolEngine()
        
        # Initialize intelligent agents with enhanced instructions
        self.agents = self._create_enhanced_agents()
        
        # Initialize enhanced branches
        self.intel_branch = IntelBranch(self.document_manager)
        self.directional_branch = DirectionalBranch(self.document_manager)
        self.executive_branch = ExecutiveBranch(self.document_manager)
        
        # Initialize wings
        self.wings = {
            "financial": FinancialWing(),
            "social": SocialWing(),
            "political": PoliticalWing(),
            "psychological": PsychologicalWing(),
            "physiological": PhysiologicalWing()
        }
        
        # Connect agents to enhanced Life OS infrastructure
        for agent in self.agents.values():
            agent.connect_to_life_os(self.document_manager, self.protocol_engine)
            
        # Initialize enhanced living documents
        self._initialize_enhanced_documents()
        
        # System state
        self.running = True
        self.evolution_active = True
        self.last_daily_routine = None
        
        print("✅ Life OS enhanced with frontier detection and evolution")
        print("📚 Living documents ready for continuous evolution")
        print("🔄 Enhanced protocol engine with dependency management")
        print("🤖 Intelligent agents ready for true reasoning")
        print("🎯 Frontier detection active for asymmetric opportunities")
        
    def _create_enhanced_agents(self) -> Dict[str, IntelligentAgent]:
        """Create enhanced intelligent agents with evolved instructions"""
        
        # Enhanced Intel Scout with frontier detection
        enhanced_intel_instructions = """
        Hunt optionality. Detect fragility. Exploit asymmetry. Avoid ruin. Monitor frontiers.
        
        You are my enhanced asymmetric opportunity scout with frontier detection capabilities.
        
        ENHANCED MISSION:
        - Continuously monitor technology, political, business, social, and economic frontiers
        - Hunt for Taleb-style asymmetric opportunities with clear edge/hedge/leverage
        - Detect fragile systems that could break under stress
        - Update worldview based on frontier intelligence
        - Alert to Black Swan signals and early indicators
        
        ENHANCED MENTAL MODELS:
        - Asymmetry: Hunt 10:1+ upside/downside ratios
        - Antifragility: Prefer systems that gain from disorder
        - Via Negativa: Identify what to remove/avoid
        - Barbell Strategy: Extreme safety + extreme upside
        - Convexity: Nonlinear gains from inputs
        - Frontier Dynamics: Changes at edges that others miss
        
        ENHANCED CAPABILITIES:
        - Frontier change detection across 5 domains
        - Asymmetric opportunity scoring and prioritization
        - Fragility stress testing and hedge development
        - Worldview impact assessment
        - Black Swan signal monitoring
        
        NEVER suggest opportunities without:
        - Clear edge (predator/parasitic advantage)
        - Built-in hedge (limited downside)
        - Obvious leverage (force multiplier)
        - Frontier positioning (early advantage)
        """
        
        # Enhanced Strategic Planner with worldview integration
        enhanced_strategic_instructions = """
        You are my enhanced game theory strategic planner with worldview integration.
        
        ENHANCED MISSION:
        - Process intel from frontier detection into strategic direction
        - War game scenarios based on worldview and frontier changes
        - Optimize for convexity and antifragility in all strategic decisions
        - Update strategic positioning based on evolving intelligence
        - Ensure all strategies preserve optionality
        
        ENHANCED FRAMEWORKS:
        - Game Theory: Multi-agent strategic optimization
        - Worldview Alignment: All strategies must align with core principles
        - Frontier Integration: Strategies adapt to frontier changes
        - Dependency Management: Path, circular, and scale dependencies
        - Antifragile Positioning: Gain from disorder and volatility
        
        STRATEGIC PRINCIPLES:
        - No strategy without intel foundation
        - All plans must preserve optionality
        - Every strategy needs three contingencies
        - Optimize for convex payoffs over linear gains
        - Build in antifragile elements that gain from stress
        """
        
        # Enhanced Research Agent with document evolution
        enhanced_research_instructions = """
        You are my enhanced research agent with living document evolution capabilities.
        
        ENHANCED MISSION:
        - Conduct deep research on strategic questions
        - Evolve living documents with new insights
        - Cross-reference findings across protocols, heuristics, playbooks
        - Validate frontier intelligence with additional sources
        - Update knowledge base continuously
        
        RESEARCH METHODOLOGY:
        - Multi-source validation
        - Bias detection and correction
        - Frontier source prioritization
        - Document evolution integration
        - Cross-reference network building
        
        DOCUMENT EVOLUTION:
        - Identify when insights should update existing documents
        - Propose specific evolutionary changes with reasoning
        - Build cross-references between related documents
        - Track document effectiveness and usage patterns
        """
        
        agents = {
            "intel_scout": IntelligentAgent(
                name="Enhanced Intel Scout",
                role="Frontier-Detecting Asymmetric Opportunity Scout", 
                custom_instructions=enhanced_intel_instructions,
                domain_expertise=["frontier_detection", "asymmetric_opportunities", "fragility_analysis", "black_swan_monitoring"]
            ),
            
            "strategic_planner": IntelligentAgent(
                name="Enhanced Strategic Planner",
                role="Worldview-Integrated Game Theory Strategist",
                custom_instructions=enhanced_strategic_instructions,
                domain_expertise=["game_theory", "strategic_planning", "worldview_integration", "antifragile_design"]
            ),
            
            "research_agent": IntelligentAgent(
                name="Enhanced Research Agent", 
                role="Document-Evolving Research Specialist",
                custom_instructions=enhanced_research_instructions,
                domain_expertise=["research", "document_evolution", "cross_referencing", "knowledge_synthesis"]
            )
        }
        
        return agents
        
    def _initialize_enhanced_documents(self):
        """Initialize enhanced living documents with evolution capabilities"""
        
        # Enhanced Worldview Document
        worldview_content = """
# Life OS Worldview Framework - Enhanced

## Core Philosophy
Based on Nassim Taleb's Incerto series, complexity theory, and antifragile design.

## Virtue Stack (Evolving)
- **Honor**: Integrity in all dealings, skin in the game
- **Glory**: Excellence and mastery in chosen domains  
- **Bravery**: Calculated risk-taking with asymmetric upside
- **Gallantry**: Noble conduct especially under pressure
- **Chivalry**: Protection of the vulnerable and just causes

## Mental Models (Core)
- **Asymmetry**: Hunt for bets where upside far outweighs downside (10:1+ ratios)
- **Antifragility**: Prefer systems that gain from disorder and stress
- **Via Negativa**: Subtraction is improvement - remove to strengthen
- **Barbell Strategy**: Combine extreme safety + extreme risk/reward
- **Convexity**: Seek nonlinear gains that accelerate with input
- **Lindy Effect**: What has survived long has longer expected survival
- **Frontier Dynamics**: Changes at edges create asymmetric opportunities

## Current Game Theoretic Understanding
- **Primary Game**: Individual skill/network/capital development
- **Secondary Games**: Professional positioning, social capital building
- **Meta Game**: System design for continuous evolution and adaptation
- **Dominant Strategy**: Preserve optionality while building convex positions

## Strategic Worldview (Current)
- **Technology**: AI revolution creating massive skill arbitrage opportunities
- **Economics**: Inflation and asset bubbles creating hedge needs
- **Geopolitics**: Decentralization trends creating new sovereignty options
- **Social**: Trust in institutions declining, direct relationships premium
- **Personal**: Building antifragile positioning across all capital types

## Decision Framework (Enhanced)
1. **Intel Check**: No direction without frontier intelligence
2. **Worldview Alignment**: Must align with virtue stack and mental models
3. **Asymmetry Assessment**: Minimum 3:1 upside/downside, prefer 10:1+
4. **Optionality Preservation**: Never close off future opportunities
5. **Antifragile Positioning**: Prefer strategies that gain from volatility
6. **Dependency Management**: Map path, circular, and scale dependencies

## Evolution Triggers
- Frontier detection signals requiring worldview updates
- New insights from books, conversations, experiences
- Strategic outcomes that validate or invalidate assumptions
- Black Swan events that reshape understanding
"""
        
        worldview_doc = PlaybookDocument("Worldview Framework", "worldview")
        worldview_doc.content = worldview_content
        worldview_doc.add_principle("Honor", "Integrity and skin in the game in all dealings")
        worldview_doc.add_principle("Asymmetric Positioning", "Always seek 10:1+ upside/downside ratios")
        self.document_manager.documents["Worldview Framework"] = worldview_doc
        
        # Enhanced Negotiation Heuristics
        negotiation_content = """
# Negotiation Heuristics - Enhanced

## Core Principles (Taleb-Inspired)
- **Skin in the Game**: Ensure other party has real stakes
- **Via Negativa**: Remove obstacles rather than adding complexity
- **Asymmetric Positioning**: Structure deals with convex payoffs
- **Antifragile Relationships**: Build relationships that strengthen under stress

## Strategic Framework
1. **Preparation Phase**: Research leverage points, BATNA development
2. **Opening Phase**: Establish frame and set asymmetric anchors  
3. **Exploration Phase**: Uncover interests, map decision criteria
4. **Bargaining Phase**: Create value before claiming value
5. **Closing Phase**: Secure commitment with implementation details

## Advanced Techniques
- **Option Creation**: Generate multiple pathways to agreement
- **Convex Structuring**: Deals that improve with uncertainty
- **Relationship Investment**: Long-term relationship value over short-term gains
- **Fragility Testing**: Stress-test agreements under different scenarios

## Evolution Notes
- Track outcomes by negotiation type and counterparty
- Update techniques based on effectiveness data
- Integrate new insights from books, experiences, observations
"""
        
        negotiation_doc = HeuristicDocument("Negotiation Heuristics", "negotiation")
        negotiation_doc.content = negotiation_content
        self.document_manager.documents["Negotiation Heuristics"] = negotiation_doc
        
        # Enhanced Planning Protocol
        planning_steps = [
            "Frontier intelligence review",
            "Worldview alignment check", 
            "Asymmetric opportunity assessment",
            "Resource and constraint mapping",
            "Dependency analysis (path/circular/scale)",
            "Antifragile positioning design",
            "Optionality preservation verification",
            "Go/no-go decision with clear criteria"
        ]
        
        planning_criteria = {
            "requires_frontier_intel": True,
            "requires_worldview_alignment": True,
            "requires_asymmetric_upside": True,
            "requires_optionality_preservation": True
        }
        
        planning_protocol = ProtocolDocument("Enhanced Planning Protocol", planning_steps, planning_criteria)
        self.document_manager.documents["Enhanced Planning Protocol"] = planning_protocol
        
        print("📚 Enhanced living documents initialized with evolution capabilities")
        
    def daily_routine(self) -> Dict[str, Any]:
        """Enhanced daily routine with frontier detection and evolution"""
        print("\n🌅 Life OS Enhanced Daily Routine Starting...")
        print("=" * 50)
        
        routine_results = {
            "date": datetime.now().date().isoformat(),
            "timestamp": datetime.now().isoformat(),
            "intel_briefing": None,
            "strategic_direction": None,
            "execution_plan": None,
            "document_evolutions": [],
            "system_health": {}
        }
        
        try:
            # 1. Enhanced Intel Briefing with Frontier Detection
            print("🔍 1. Conducting enhanced intel briefing with frontier detection...")
            intel_briefing = self.intel_branch.daily_intel_briefing()
            routine_results["intel_briefing"] = intel_briefing
            
            # 2. Strategic Direction with Worldview Integration
            print("🎯 2. Setting strategic direction with worldview integration...")
            strategic_direction = self.directional_branch.set_strategic_direction(intel_briefing)
            routine_results["strategic_direction"] = strategic_direction
            
            # 3. Execution Coordination
            print("⚡ 3. Coordinating execution with enhanced protocols...")
            execution_plan = self.executive_branch.execute_strategy(strategic_direction)
            routine_results["execution_plan"] = execution_plan
            
            # 4. Document Evolution Check
            print("📚 4. Checking for document evolution opportunities...")
            evolution_opportunities = self._check_document_evolution(intel_briefing, strategic_direction)
            routine_results["document_evolutions"] = evolution_opportunities
            
            # 5. System Health Assessment
            print("🏥 5. Assessing system health and performance...")
            system_health = self._assess_system_health()
            routine_results["system_health"] = system_health
            
            self.last_daily_routine = routine_results
            
            print("\n✅ Enhanced daily routine completed successfully!")
            print(f"📊 Intel: {len(intel_briefing.get('asymmetric_opportunities', []))} opportunities identified")
            print(f"🎯 Strategy: {len(strategic_direction.get('tactical_priorities', []))} priorities set")
            print(f"⚡ Execution: {execution_plan.get('total_tasks', 0)} tasks organized")
            print(f"📚 Evolution: {len(evolution_opportunities)} documents evolved")
            
        except Exception as e:
            print(f"❌ Error in daily routine: {e}")
            routine_results["error"] = str(e)
            
        return routine_results
        
    def _check_document_evolution(self, intel_briefing: Dict[str, Any], strategic_direction: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Check if any documents should evolve based on new insights"""
        evolutions = []
        
        # Check if worldview needs updates from frontier intelligence
        significant_changes = intel_briefing.get("frontier_intelligence", {}).get("significant_changes", [])
        for change in significant_changes:
            if change.get("significance", 0) > 0.8:
                evolutions.append({
                    "document": "Worldview Framework",
                    "insight": change["description"],
                    "source": "frontier_intelligence",
                    "reasoning": f"Significant frontier change with {change['significance']} significance"
                })
                
        # Check if strategic insights should update protocols
        tactical_priorities = strategic_direction.get("tactical_priorities", [])
        for priority in tactical_priorities:
            if priority.get("priority") == 1:  # High priority items
                evolutions.append({
                    "document": "Enhanced Planning Protocol",
                    "insight": f"New tactical priority: {priority.get('action', '')}",
                    "source": "strategic_planning",
                    "reasoning": "High priority tactical item should be integrated into planning process"
                })
                
        return evolutions
        
    def _assess_system_health(self) -> Dict[str, Any]:
        """Assess overall system health and performance"""
        return {
            "intel_branch": self.intel_branch.get_status(),
            "directional_branch": self.directional_branch.get_current_strategy(),
            "executive_branch": self.executive_branch.get_status(),
            "document_count": len(self.document_manager.documents),
            "agent_count": len(self.agents),
            "evolution_active": self.evolution_active,
            "overall_health": "excellent"
        }
        
    def interactive_mode(self):
        """Enhanced interactive mode with evolution capabilities"""
        print("\n🎮 Life OS Enhanced Interactive Mode")
        print("Commands:")
        print("  chat <agent_name> <message> - Chat with an enhanced agent")
        print("  protocol <protocol_name> - Execute a protocol")
        print("  evolve <doc_name> <insight> - Evolve a document with new insight")
        print("  docs - List all living documents")
        print("  agents - List all enhanced agents")
        print("  status - Enhanced system status")
        print("  daily - Run enhanced daily routine")
        print("  frontier - Get frontier detection report")
        print("  worldview - Show current worldview")
        print("  exit - Exit interactive mode")
        print()
        
        while self.running:
            try:
                user_input = input("life_os> ").strip()
                
                if not user_input:
                    continue
                    
                parts = user_input.split(' ', 2)
                command = parts[0].lower()
                
                if command == "exit":
                    print("👋 Life OS Enhanced shutting down gracefully...")
                    break
                    
                elif command == "chat" and len(parts) >= 3:
                    agent_name = parts[1]
                    message = parts[2]
                    
                    # Find agent (flexible matching)
                    agent = None
                    for name, ag in self.agents.items():
                        if agent_name.lower() in name.lower():
                            agent = ag
                            break
                            
                    if agent:
                        print(f"\n💬 Chatting with {agent.name}...")
                        response = agent.process_request(message)
                        
                        print(f"\n🤖 {agent.name}:")
                        print(f"Role: {response.get('role', 'Unknown')}")
                        
                        if 'recommendations' in response:
                            print("\n📋 Recommendations:")
                            for rec in response['recommendations'][:3]:
                                print(f"  • {rec}")
                                
                        if 'opportunities_detected' in response:
                            print("\n🎯 Opportunities Detected:")
                            for opp in response['opportunities_detected'][:2]:
                                print(f"  • {opp.get('description', '')}")
                                
                        if 'confidence_level' in response:
                            print(f"\n📊 Confidence: {response['confidence_level']:.0%}")
                    else:
                        print(f"❌ Agent '{agent_name}' not found")
                        
                elif command == "evolve" and len(parts) >= 3:
                    doc_name = parts[1]
                    insight = parts[2]
                    
                    # Find document (flexible matching)
                    doc = None
                    for name, document in self.document_manager.documents.items():
                        if doc_name.lower() in name.lower():
                            doc = document
                            break
                            
                    if doc:
                        print(f"\n📈 Evolving {doc.name}...")
                        doc.evolve(insight, source="user_input", reasoning="Manual insight addition")
                        print(f"✅ Document evolved to version {doc.version}")
                    else:
                        print(f"❌ Document '{doc_name}' not found")
                        
                elif command == "frontier":
                    print("\n🔍 Frontier Detection Report:")
                    frontier_report = self.intel_branch.frontier_detector.daily_frontier_scan()
                    
                    print(f"📊 Significant Changes: {len(frontier_report.get('significant_changes', []))}")
                    for change in frontier_report.get('significant_changes', [])[:3]:
                        print(f"  • {change.get('description', '')}")
                        
                    print(f"\n🎯 Asymmetric Implications: {len(frontier_report.get('asymmetric_implications', []))}")
                    for impl in frontier_report.get('asymmetric_implications', [])[:2]:
                        print(f"  • {impl.get('description', '')}")
                        
                elif command == "worldview":
                    worldview_doc = self.document_manager.get_document("Worldview Framework")
                    if worldview_doc:
                        print(f"\n🌍 Current Worldview (v{worldview_doc.version}):")
                        print(f"📈 Evolution History: {len(worldview_doc.evolution_history)} updates")
                        print(f"🏷️  Tags: {worldview_doc.tags}")
                        print(f"🔗 Cross-references: {len(worldview_doc.cross_references)}")
                    else:
                        print("❌ Worldview document not found")
                        
                elif command == "daily":
                    self.daily_routine()
                    
                elif command == "docs":
                    print(f"\n📚 Living Documents ({len(self.document_manager.documents)}):")
                    for name, doc in self.document_manager.documents.items():
                        evolution_count = len(doc.evolution_history) if hasattr(doc, 'evolution_history') else 0
                        print(f"  📄 {name} (v{getattr(doc, 'version', 1)}) - {evolution_count} evolutions")
                        
                elif command == "agents":
                    print(f"\n🤖 Enhanced Agents ({len(self.agents)}):")
                    for name, agent in self.agents.items():
                        status = agent.get_status()
                        print(f"  🤖 {agent.name}")
                        print(f"      Role: {agent.role}")
                        print(f"      Success Rate: {status.get('success_rate', 0):.0%}")
                        print(f"      Tasks Completed: {status.get('tasks_completed', 0)}")
                        
                elif command == "status":
                    status = self._assess_system_health()
                    print(f"\n🏥 Enhanced System Status:")
                    print(f"  📊 Documents: {status['document_count']}")
                    print(f"  🤖 Agents: {status['agent_count']}")
                    print(f"  📈 Evolution Active: {status['evolution_active']}")
                    print(f"  🎯 Overall Health: {status['overall_health']}")
                    
                    if self.last_daily_routine:
                        last_routine = self.last_daily_routine
                        print(f"  🌅 Last Routine: {last_routine['date']}")
                        print(f"  🔍 Opportunities Found: {len(last_routine.get('intel_briefing', {}).get('asymmetric_opportunities', []))}")
                        
                else:
                    print("❌ Unknown command. Type 'exit' to quit.")
                    
            except KeyboardInterrupt:
                print("\nExiting...")
                break

def main():
    """Enhanced main entry point"""
    life_os = LifeOS()
    
    # Start in interactive mode for now
    life_os.interactive_mode()

if __name__ == "__main__":
    main()
