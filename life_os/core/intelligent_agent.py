"""
Intelligent Agent - True reasoning agents with dynamic instruction following
"""
from crewai import Agent
from langchain_huggingface import HuggingFaceEndpoint
import os
import json
from typing import Dict, Any, List
from datetime import datetime
from .document_manager import DocumentManager
from .protocol_engine import ProtocolEngine


class IntelligentAgent(Agent):
    """
    A truly intelligent agent that integrates CrewAI and Hugging Face LLM
    """

    def __init__(self,
                 name: str,
                 role: str,
                 custom_instructions: str,
                 domain_expertise: List[str] = None):
        llm = HuggingFaceEndpoint(
            repo_id=os.getenv("HF_MODEL",
                              "mistralai/Mistral-7B-Instruct-v0.2"),
            huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
            temperature=0.7,
            max_new_tokens=500)
        super().__init__(
            role=role,
            goal=custom_instructions,
            backstory=
            f"Expert in {', '.join(domain_expertise or [])} with a focus on antifragile strategies.",
            llm=llm,
            verbose=True)
        self._custom_data = {
            "agent_name": name,
            "domain_expertise": domain_expertise or [],
            "conversation_memory": [],
            "long_term_memory": {},
            "working_memory": {},
            "expertise_level": {},
            "tasks_completed": 0,
            "success_rate": 0.0,
            "expertise_growth": {},
            "document_manager": None,
            "protocol_engine": None
        }

    @property
    def name(self) -> str:
        return self._custom_data["agent_name"]

    @property
    def domain_expertise(self) -> List[str]:
        return self._custom_data["domain_expertise"]

    def connect_to_life_os(self, doc_manager: DocumentManager,
                           protocol_engine: ProtocolEngine):
        self._custom_data["document_manager"] = doc_manager
        self._custom_data["protocol_engine"] = protocol_engine

    def process_request(self,
                        request: str,
                        context: Dict[str, Any] = None) -> Dict[str, Any]:
        reasoning_context = self._build_reasoning_context(request, context)
        response = self._reason_through_request(request, reasoning_context)
        self._update_memory(request, response, context)
        return response

    def _build_reasoning_context(self, request: str,
                                 context: Dict[str, Any]) -> Dict[str, Any]:
        reasoning_context = {
            "request": request,
            "external_context": context or {},
            "agent_instructions": self.goal,
            "domain_expertise": self._custom_data["domain_expertise"],
            "relevant_documents": [],
            "applicable_protocols": [],
            "past_similar_requests": []
        }
        doc_manager = self._custom_data["document_manager"]
        if doc_manager:
            relevant_docs = doc_manager.search_documents(request)
            reasoning_context["relevant_documents"] = [
                doc.to_dict() for doc in relevant_docs[:3]
            ]
        protocol_engine = self._custom_data["protocol_engine"]
        if protocol_engine and ("plan" in request.lower()
                                or "execute" in request.lower()):
            optimal_workflow = protocol_engine.get_optimal_workflow(
                request, context or {})
            reasoning_context["applicable_protocols"] = optimal_workflow
        reasoning_context[
            "past_similar_requests"] = self._find_similar_requests(request)
        return reasoning_context

    def _reason_through_request(
            self, request: str,
            reasoning_context: Dict[str, Any]) -> Dict[str, Any]:
        try:
            prompt = (
                f"Role: {self.role}\n"
                f"Instructions: {self.goal}\n"
                f"Expertise: {', '.join(self._custom_data['domain_expertise'])}\n"
                f"Context: {json.dumps(reasoning_context, indent=2)}\n"
                f"Request: {request}\n"
                f"Provide a concise response with recommendations and detected opportunities."
            )
            response = self.llm.invoke(prompt)
            reasoning_steps = [
                "Context analysis", "LLM reasoning", "Response generation"
            ]
            opportunities = []
            recommendations = [
                response[:100] + "..." if len(response) > 100 else response
            ]
            if "opportunity" in response.lower():
                opportunities.append({
                    "description": response,
                    "asymmetry_ratio": "5:1"
                })
            return {
                "agent": self._custom_data["agent_name"],
                "role": self.role,
                "reasoning_process": reasoning_steps,
                "opportunities_detected": opportunities,
                "recommendations": recommendations,
                "confidence_level": 0.9
            }
        except Exception as e:
            return {
                "agent": self._custom_data["agent_name"],
                "role": self.role,
                "error": f"LLM request failed: {str(e)}",
                "confidence_level": 0.0
            }

    def _update_memory(self, request: str, response: Dict[str, Any],
                       context: Dict[str, Any]):
        interaction = {
            "timestamp": datetime.now().isoformat(),
            "request": request,
            "response": response,
            "context": context,
            "success": response.get("confidence_level", 0) > 0.7
        }
        self._custom_data["conversation_memory"].append(interaction)
        if len(self._custom_data["conversation_memory"]) > 50:
            self._custom_data["conversation_memory"] = self._custom_data[
                "conversation_memory"][-50:]
        successful_interactions = sum(
            1 for i in self._custom_data["conversation_memory"]
            if i["success"])
        self._custom_data["success_rate"] = successful_interactions / len(
            self._custom_data["conversation_memory"])

    def _find_similar_requests(self, request: str) -> List[Dict[str, Any]]:
        similar = []
        request_words = set(request.lower().split())
        for interaction in self._custom_data["conversation_memory"][-10:]:
            past_words = set(interaction["request"].lower().split())
            similarity = len(request_words.intersection(past_words)) / len(
                request_words.union(past_words))
            if similarity > 0.3:
                similar.append({
                    "request": interaction["request"],
                    "response": interaction["response"],
                    "similarity": similarity
                })
        return sorted(similar, key=lambda x: x["similarity"], reverse=True)[:3]

    def get_status(self) -> Dict[str, Any]:
        return {
            "name":
            self._custom_data["agent_name"],
            "role":
            self.role,
            "tasks_completed":
            self._custom_data["tasks_completed"],
            "success_rate":
            self._custom_data["success_rate"],
            "memory_size":
            len(self._custom_data["conversation_memory"]),
            "domain_expertise":
            self._custom_data["domain_expertise"],
            "connected_to_life_os":
            self._custom_data["document_manager"] is not None
        }
