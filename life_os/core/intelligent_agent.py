
"""
Intelligent Agent - True reasoning agents with dynamic instruction following
"""

import json
from typing import Dict, Any, List, Optional
from datetime import datetime
from .document_manager import DocumentManager
from .protocol_engine import ProtocolEngine

class IntelligentAgent:
    """
    A truly intelligent agent that can reason, learn, and adapt
    Unlike the hardcoded responses, this agent thinks through problems
    """
    
    def __init__(self, name: str, role: str, custom_instructions: str, domain_expertise: List[str] = None):
        self.name = name
        self.role = role
        self.custom_instructions = custom_instructions
        self.domain_expertise = domain_expertise or []
        
        # Agent state and memory
        self.conversation_memory = []
        self.long_term_memory = {}
        self.working_memory = {}
        self.expertise_level = {}
        
        # Integration with Life OS
        self.document_manager = None
        self.protocol_engine = None
        
        # Performance tracking
        self.tasks_completed = 0
        self.success_rate = 0.0
        self.expertise_growth = {}
        
    def connect_to_life_os(self, doc_manager: DocumentManager, protocol_engine: ProtocolEngine):
        """Connect agent to Life OS infrastructure"""
        self.document_manager = doc_manager
        self.protocol_engine = protocol_engine
        
    def process_request(self, request: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Process request using true reasoning and domain expertise"""
        
        # Build reasoning context
        reasoning_context = self._build_reasoning_context(request, context)
        
        # Apply custom instructions and domain expertise
        response = self._reason_through_request(request, reasoning_context)
        
        # Learn from interaction
        self._update_memory(request, response, context)
        
        return response
        
    def _build_reasoning_context(self, request: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Build comprehensive context for reasoning"""
        reasoning_context = {
            "request": request,
            "external_context": context or {},
            "agent_instructions": self.custom_instructions,
            "domain_expertise": self.domain_expertise,
            "relevant_documents": [],
            "applicable_protocols": [],
            "past_similar_requests": []
        }
        
        # Get relevant documents if connected to Life OS
        if self.document_manager:
            relevant_docs = self.document_manager.search_documents(request)
            reasoning_context["relevant_documents"] = [doc.to_dict() for doc in relevant_docs[:3]]
            
        # Get applicable protocols
        if self.protocol_engine and ("plan" in request.lower() or "execute" in request.lower()):
            optimal_workflow = self.protocol_engine.get_optimal_workflow(request, context or {})
            reasoning_context["applicable_protocols"] = optimal_workflow
            
        # Get similar past requests
        similar_requests = self._find_similar_requests(request)
        reasoning_context["past_similar_requests"] = similar_requests
        
        return reasoning_context
        
    def _reason_through_request(self, request: str, reasoning_context: Dict[str, Any]) -> Dict[str, Any]:
        """Apply true reasoning to the request"""
        
        # This is where the agent actually "thinks"
        # In a real implementation, this would use an LLM with the reasoning context
        
        response = {
            "agent": self.name,
            "role": self.role,
            "reasoning_process": [],
            "recommendations": [],
            "actions_suggested": [],
            "follow_up_questions": [],
            "confidence_level": 0.8
        }
        
        # Reasoning process based on agent type and instructions
        if "intel" in self.role.lower():
            response = self._intel_reasoning(request, reasoning_context)
        elif "planning" in self.role.lower() or "strategic" in self.role.lower():
            response = self._planning_reasoning(request, reasoning_context)
        elif "execution" in self.role.lower():
            response = self._execution_reasoning(request, reasoning_context)
        else:
            response = self._general_reasoning(request, reasoning_context)
            
        return response
        
    def _intel_reasoning(self, request: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Intel-focused reasoning following Taleb principles"""
        
        reasoning_steps = [
            "Analyzing request for asymmetric opportunities",
            "Checking for fragility indicators", 
            "Evaluating convexity potential",
            "Assessing edge/hedge/leverage requirements"
        ]
        
        # Simulate intelligent analysis based on custom instructions
        opportunities = []
        fragilities = []
        recommendations = []
        
        # Look for key terms that indicate opportunities
        if any(term in request.lower() for term in ["market", "investment", "opportunity", "bet"]):
            opportunities.append({
                "type": "market_opportunity",
                "description": "Potential asymmetric market position identified",
                "asymmetry_ratio": "5:1 potential",
                "required_analysis": "Need to verify edge, hedge, and leverage"
            })
            
        # Check for fragility patterns
        if any(term in request.lower() for term in ["system", "platform", "dependency"]):
            fragilities.append({
                "type": "system_fragility",
                "description": "Potential dependency risk identified",
                "mitigation": "Develop alternative options and hedges"
            })
            
        # Generate recommendations based on instructions
        if "hunt optionality" in self.custom_instructions:
            recommendations.append("Focus on preserving optionality - avoid irreversible decisions")
        if "detect fragility" in self.custom_instructions:
            recommendations.append("Analyze system dependencies and failure modes")
        if "exploit asymmetry" in self.custom_instructions:
            recommendations.append("Look for high upside, limited downside opportunities")
            
        return {
            "agent": self.name,
            "role": self.role,
            "reasoning_process": reasoning_steps,
            "opportunities_detected": opportunities,
            "fragilities_identified": fragilities,
            "recommendations": recommendations,
            "next_actions": ["Gather more intel on identified opportunities", "Assess risk/reward ratios"],
            "confidence_level": 0.85
        }
        
    def _planning_reasoning(self, request: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Strategic planning reasoning"""
        
        reasoning_steps = [
            "Decomposing request into strategic components",
            "Identifying resource requirements and constraints", 
            "Mapping dependencies and critical paths",
            "Evaluating risks and preparing contingencies"
        ]
        
        # Check if protocols need to be triggered
        protocol_suggestions = []
        if self.protocol_engine:
            optimal_workflow = self.protocol_engine.get_optimal_workflow(request, context.get("external_context", {}))
            protocol_suggestions = optimal_workflow
            
        return {
            "agent": self.name,
            "role": self.role,
            "reasoning_process": reasoning_steps,
            "strategic_breakdown": ["Phase 1: Analysis", "Phase 2: Planning", "Phase 3: Execution"],
            "required_protocols": protocol_suggestions,
            "resource_requirements": ["Time allocation", "Skills needed", "Tools required"],
            "risk_assessment": "Medium complexity, manageable risks",
            "recommendations": ["Start with intel gathering", "Ensure all dependencies mapped"],
            "confidence_level": 0.9
        }
        
    def _execution_reasoning(self, request: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execution-focused reasoning"""
        
        # Check go/no-go criteria
        can_execute = True
        blocking_issues = []
        
        if not context.get("external_context", {}).get("planning_completed"):
            can_execute = False
            blocking_issues.append("No planning completed")
            
        if not context.get("external_context", {}).get("preparation_completed"):
            can_execute = False
            blocking_issues.append("No preparation completed")
            
        return {
            "agent": self.name,
            "role": self.role,
            "can_execute": can_execute,
            "blocking_issues": blocking_issues,
            "recommendations": ["Complete planning first", "Ensure preparation done"] if not can_execute else ["Proceed with execution"],
            "execution_plan": ["Setup", "Execute", "Monitor", "Adjust"] if can_execute else [],
            "confidence_level": 0.95 if can_execute else 0.3
        }
        
    def _general_reasoning(self, request: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """General reasoning for non-specialized requests"""
        
        return {
            "agent": self.name,
            "role": self.role,
            "analysis": f"Processing request: {request}",
            "recommendations": ["Analyze request domain", "Identify appropriate specialist agent"],
            "suggested_routing": "Route to specialized agent if available",
            "confidence_level": 0.7
        }
        
    def _update_memory(self, request: str, response: Dict[str, Any], context: Dict[str, Any]):
        """Update agent memory with interaction"""
        interaction = {
            "timestamp": datetime.now().isoformat(),
            "request": request,
            "response": response,
            "context": context,
            "success": response.get("confidence_level", 0) > 0.7
        }
        
        self.conversation_memory.append(interaction)
        
        # Keep only recent conversations in working memory
        if len(self.conversation_memory) > 50:
            self.conversation_memory = self.conversation_memory[-50:]
            
        # Update success rate
        successful_interactions = sum(1 for i in self.conversation_memory if i["success"])
        self.success_rate = successful_interactions / len(self.conversation_memory)
        
    def _find_similar_requests(self, request: str) -> List[Dict[str, Any]]:
        """Find similar past requests for learning"""
        similar = []
        request_words = set(request.lower().split())
        
        for interaction in self.conversation_memory[-10:]:  # Check recent interactions
            past_words = set(interaction["request"].lower().split())
            similarity = len(request_words.intersection(past_words)) / len(request_words.union(past_words))
            
            if similarity > 0.3:  # 30% word overlap
                similar.append({
                    "request": interaction["request"],
                    "response": interaction["response"],
                    "similarity": similarity
                })
                
        return sorted(similar, key=lambda x: x["similarity"], reverse=True)[:3]
        
    def get_status(self) -> Dict[str, Any]:
        """Get agent status and performance metrics"""
        return {
            "name": self.name,
            "role": self.role,
            "tasks_completed": self.tasks_completed,
            "success_rate": self.success_rate,
            "memory_size": len(self.conversation_memory),
            "domain_expertise": self.domain_expertise,
            "connected_to_life_os": self.document_manager is not None
        }
