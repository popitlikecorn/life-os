import spacy
from loguru import logger
import yaml
from life_os.agents.agent_coordinator import AgentCoordinator
from life_os.core.living_document import LivingDocument
from datetime import datetime


class LifeOS:

    def __init__(self):
        logger.add("life_os/logs/execution.log", rotation="1 MB")
        logger.info("Initializing Life OS")
        # Load intent classifier
        try:
            self.nlp = spacy.load("life_os/models/intent_classifier")
            print(
                f"Loaded intent_classifier with pipelines: {self.nlp.pipe_names}"
            )
        except Exception as e:
            logger.error(f"Failed to load intent_classifier: {e}")
            self.nlp = spacy.load("en_core_web_sm")
            print("Fallback to en_core_web_sm")
        # Initialize agents and living document
        self.coordinator = AgentCoordinator()
        self.worldview_doc = LivingDocument(
            "Worldview", "worldview", content="Initial worldview framework")
        self._load_agents()

    def _load_agents(self):
        try:
            with open("life_os/config/agents.yaml", "r") as f:
                agent_configs = yaml.safe_load(f)
                logger.info(f"Loaded agents.yaml: {agent_configs}")
                print("🤖 Initializing AI agents...")
                for agent_name, config in agent_configs.items():
                    capabilities = config.get("capabilities", [])
                    role = config.get("role", agent_name)
                    instructions = config.get("instructions", "")
                    self.coordinator.create_custom_agent({
                        "name":
                        agent_name,
                        "role":
                        role,
                        "instructions":
                        instructions,
                        "capabilities":
                        capabilities
                    })
                    print(f"  ✅ Initialized {agent_name}")
        except Exception as e:
            logger.error(f"Failed to load agents.yaml: {e}")
            print("⚠️ Using fallback agents")
            self.coordinator.setup_default_agents()
        print("✅ System ready.")

    def process_query(self, query):
        logger.info(f"Query: {query}")
        doc = self.nlp(query.lower())
        if "textcat" in self.nlp.pipe_names:
            intent = max(doc.cats, key=doc.cats.get)
            confidence = doc.cats[intent]
            logger.info(
                f"Intent: {intent}, Confidence: {confidence}, Scores: {doc.cats}"
            )
            if confidence < 0.3:
                logger.warning(
                    f"Low confidence for intent {intent}: {confidence}")
        else:
            logger.warning("Textcat missing, using fallback")
            tokens = [token.text for token in doc]
            if any(t in ["whats", "yo", "hello", "hi", "hey"] for t in tokens):
                intent = "greet"
            elif any(t == "crew" for t in tokens):
                intent = "crew"
            elif any(t in ["exit", "quit", "shutdown", "bye"] for t in tokens):
                intent = "exit"
            elif "affair" in query.lower() or "interest" in query.lower():
                intent = "affairs"
            else:
                intent = "unknown"
        try:
            if intent == "greet":
                return "Ready to execute, commander."
            elif intent == "crew":
                return self.run_crew_operations()
            elif intent == "exit":
                logger.info("System shutdown")
                return "System shutdown."
            elif intent == "affairs":
                return self.handle_affairs(query)
            else:
                return "Unknown query. Retry."
        except Exception as e:
            logger.error(f"Query error: {e}")
            return f"Error: {str(e)}."

    def run_crew_operations(self):
        print("🚀 Starting crew operations...")
        try:
            print("🤖 Initializing agents...")
            for agent_name in self.coordinator.factory.list_agents():
                print(f"  ✅ Initialized {agent_name}")
            print("\n📊 Intel Scout scanning...")
            intel_response = self.coordinator.process_multi_agent_query(
                "Gather frontier intel", ["intel_scout"])
            self.worldview_doc.evolve(
                f"Intel update: {intel_response.get('intel_scout', '')}",
                source="intel_scout")
            print("📈 Worldview updated.")
            print("🧠 Game Theorist strategizing...")
            strategy_response = self.coordinator.process_multi_agent_query(
                "Formulate strategy", ["game_theorist"])
            print("⚙️ Ops Planner executing...")
            ops_response = self.coordinator.process_multi_agent_query(
                "Plan execution", ["ops_planner"])
            return f"Operations complete: {intel_response}, {strategy_response}, {ops_response}"
        except Exception as e:
            logger.error(f"Crew error: {e}")
            return f"Error: {str(e)}."

    def handle_affairs(self, query):
        print("🔎 Processing affairs...")
        self.worldview_doc.mark_usage(context=query)
        affair_type = "General" if "affair" in query.lower() else "Interests"
        return f"{affair_type}: {self.worldview_doc.content}. Usage count: {self.worldview_doc.usage_count}"

    def interactive_mode(self):
        print("🚀 Initializing Life OS")
        print("🧠 Enter query (e.g., 'affairs', 'crew', 'exit')")
        while True:
            try:
                query = input("life_os> ").strip()
                if query:
                    response = self.process_query(query)
                    print(response)
                    if response == "System shutdown.":
                        break
            except KeyboardInterrupt:
                logger.info("Shutdown via KeyboardInterrupt")
                print("\nSystem shutdown.")
                break


def main():
    life_os = LifeOS()
    life_os.interactive_mode()


if __name__ == "__main__":
    main()
    # import spacy
# from loguru import logger
# import yaml
# import sys
# from life_os.agents.agent_coordinator import AgentCoordinator
# from datetime import datetime

# class LifeOS:

#     def __init__(self):
#         """Initialize Life OS with intent classifier and agents."""
#         logger.add("life_os/logs/execution.log", rotation="1 MB")
#         logger.info("Initializing Life OS")

#         # Load intent classifier
#         try:
#             self.nlp = spacy.load("life_os/models/intent_classifier")
#             print(
#                 f"Loaded intent_classifier with pipelines: {self.nlp.pipe_names}"
#             )
#         except Exception as e:
#             logger.error(f"Failed to load intent_classifier: {e}")
#             self.nlp = spacy.load("en_core_web_sm")
#             logger.warning("Using en_core_web_sm as fallback")
#             print("Fallback to en_core_web_sm")

#         # Initialize agents
#         self.coordinator = AgentCoordinator()
#         self._load_agents()

#     # main.py (partial, replace _load_agents)
#     def _load_agents(self):
#         """Load agent configurations from agents.yaml."""
#         try:
#             with open("life_os/config/agents.yaml", "r") as f:
#                 agent_configs = yaml.safe_load(f)
#                 logger.info(f"Loaded agents.yaml: {agent_configs}")
#                 print("🤖 Initializing AI agents...")
#                 for agent_name, config in agent_configs.items():
#                     capabilities = config.get("capabilities", [])
#                     role = config.get("role", agent_name)
#                     instructions = config.get("instructions", "")
#                     self.coordinator.create_custom_agent({
#                         "name":
#                         agent_name,
#                         "role":
#                         role,
#                         "instructions":
#                         instructions,
#                         "capabilities":
#                         capabilities
#                     })
#                     print(f"  ✅ Initialized {agent_name}")
#         except Exception as e:
#             logger.error(f"Failed to load agents.yaml: {e}")
#             print("⚠️ Invalid or missing agent_configs, using fallback")
#             self.coordinator.setup_default_agents()
#             print("🏗️ Setting up default agent network...")
#             print(
#                 "✅ Created agent: Intel Scout (Asymmetric Opportunity Scout)")
#             print(
#                 "✅ Created agent: Strategic Planner (Strategic Planner - life_optimization)"
#             )
#             print(
#                 "✅ Created agent: Research Specialist (Research Specialist - opportunities)"
#             )
#             print("🔗 Connected Intel Scout ↔ Strategic Planner (intel_feed)")
#             print(
#                 "🔗 Connected Research Specialist ↔ Intel Scout (data_support)")
#             print(
#                 "🔗 Connected Strategic Planner ↔ Research Specialist (validation)"
#             )
#             print("✅ Default agent network established")
#         print("✅ System ready. Hunting optionality.")

#     def process_query(self, query):
#         """Process user query using intent classifier."""
#         logger.info(f"Query: {query}")
#         doc = self.nlp(query.lower())

#         # If using intent_classifier, get predicted intent
#         if "textcat" in self.nlp.pipe_names:
#             intent = max(doc.cats, key=doc.cats.get)
#             confidence = doc.cats[intent]
#             if confidence < 0.7:  # Threshold for low confidence
#                 return "Unknown query. Subtract noise. Try again."
#         else:
#             # Fallback keyword matching
#             if any(token.text in ["whats", "yo", "hello"] for token in doc):
#                 intent = "greet"
#             elif any(token.text == "crew" for token in doc):
#                 intent = "crew"
#             elif any(token.text in ["exit", "quit"] for token in doc):
#                 intent = "exit"
#             elif "affairs" in query.lower():
#                 intent = "affairs"
#             else:
#                 intent = "unknown"

#         try:
#             if intent == "greet":
#                 return "Yo, predator! Ready to hunt optionality?"
#             elif intent == "crew":
#                 return self.run_crew_operations()
#             elif intent == "exit":
#                 logger.info("System shutdown")
#                 return "System shutdown. Stay antifragile."
#             elif intent == "affairs":
#                 return self.handle_affairs()
#             else:
#                 return "Unknown query. Subtract noise. Try again."
#         except Exception as e:
#             logger.error(f"Query error: {e}")
#             return f"Fragility detected: {str(e)}. Invert. Always invert."

#     def run_crew_operations(self):
#         """Run crew operations with coordinated agents."""
#         print("🚀 Starting Life OS crew operations...")
#         try:
#             print("🤖 Initializing AI agents...")
#             for agent_name in self.coordinator.factory.list_agents():
#                 print(f"  ✅ Initialized {agent_name}")

#             print("\n🎯 Starting strategic coordination...")
#             print("📊 Intel Scout gathering intelligence...")
#             print("🔎 Intel: Scanning frontiers...")
#             print("🔍 Frontier Detector: Scanning ['tech', 'markets', 'x']...")
#             print("🔍 Frontier Detector: Scanning all frontiers...")
#             print("✅ Frontier scan complete. 0 significant changes detected.")
#             print("🧠 Intel: Processing intelligence...")
#             print(
#                 f"📈 Worldview Framework evolved to v{datetime.now().strftime('%Y%m%d')}: {{'timestamp': '{datetime.now().isoformat()}', 'oppor..."
#             )
#             print("🧠 Game Theorist developing strategy...")
#             print("⚙️ Ops Coordinator planning execution...")
#             print("🔍 Evaluating protocol: Enhanced Planning Protocol")
#             print("    ✅ Criterion passed: requires_frontier_intel = True")
#             print(
#                 "    ✅ Criterion passed: requires_worldview_alignment = True")
#             print("    ✅ Criterion passed: requires_asymmetric_upside = True")
#             print("⚙️ Executing protocol: Enhanced Planning Protocol")
#             return "Crew operations complete. Ready for next query."
#         except Exception as e:
#             logger.error(f"Crew error: {e}")
#             return f"Fragility detected: {str(e)}. Invert. Always invert."

#     def handle_affairs(self):
#         """Handle affairs query."""
#         print("🔎 Intel: Scanning frontiers...")
#         print("🔍 Frontier Detector: Scanning ['tech', 'markets', 'x']...")
#         print("🔍 Frontier Detector: Scanning all frontiers...")
#         print("✅ Frontier scan complete. 0 significant changes detected.")
#         print("🧠 Intel: Processing intelligence...")
#         print(
#             f"📈 Worldview Framework evolved to v{datetime.now().strftime('%Y%m%d')}: {{\"timestamp\": \"{datetime.now().isoformat()}\", \"oppor..."
#         )
#         return "Affairs/Interests: Honor, Glory, Bravery. X Front: []"

#     def interactive_mode(self):
#         """Run interactive CLI loop."""
#         print("🚀 Initializing Life OS - Antifragile Intelligence")
#         print(
#             "🧠 Enter any query (e.g., 'What are my affairs?', 'Daily briefing', 'exit')"
#         )
#         while True:
#             try:
#                 query = input("life_os> ").strip()
#                 if query:
#                     response = self.process_query(query)
#                     print(response)
#                     if response == "System shutdown. Stay antifragile.":
#                         break
#             except KeyboardInterrupt:
#                 logger.info("System shutdown via KeyboardInterrupt")
#                 print("\nSystem shutdown. Stay antifragile.")
#                 break
#             except Exception as e:
#                 logger.error(f"Interactive mode error: {e}")
#                 print(f"Fragility detected: {str(e)}. Invert. Always invert.")

# def main():
#     """Main entry point."""
#     life_os = LifeOS()
#     life_os.interactive_mode()

# if __name__ == "__main__":
#     main()
