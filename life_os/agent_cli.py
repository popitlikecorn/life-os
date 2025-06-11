
"""
Agent CLI - Command line interface for interacting with Life OS agents
"""

from agents.agent_coordinator import AgentCoordinator

class AgentCLI:
    """Command line interface for agent management"""
    
    def __init__(self):
        self.coordinator = AgentCoordinator()
        self.coordinator.setup_default_agents()
        
    def run(self):
        """Run the interactive CLI"""
        print("🤖 Life OS Agent CLI")
        print("=" * 40)
        print("Commands:")
        print("  list - List all agents")
        print("  create - Create a new agent")
        print("  query <agent_name> <question> - Query an agent")
        print("  workflow <workflow_name> <query> - Run a workflow")
        print("  exit - Exit CLI")
        print()
        
        while True:
            try:
                command = input("agent> ").strip()
                
                if command == "exit":
                    break
                elif command == "list":
                    self._list_agents()
                elif command.startswith("create"):
                    self._create_agent_interactive()
                elif command.startswith("query"):
                    self._query_agent(command)
                elif command.startswith("workflow"):
                    self._run_workflow(command)
                else:
                    print("Unknown command. Type 'exit' to quit.")
                    
            except KeyboardInterrupt:
                print("\nExiting...")
                break
    
    def _list_agents(self):
        """List all available agents"""
        agents = self.coordinator.factory.list_agents()
        print("\n📋 Available Agents:")
        for agent_name in agents:
            agent = self.coordinator.factory.get_agent(agent_name)
            print(f"  • {agent_name} ({agent.role})")
        print()
    
    def _create_agent_interactive(self):
        """Interactive agent creation"""
        print("\n🏗️ Create New Agent")
        name = input("Agent name: ")
        role = input("Agent role: ")
        print("Agent instructions (end with empty line):")
        
        instructions = []
        while True:
            line = input()
            if line == "":
                break
            instructions.append(line)
        
        instruction_text = "\n".join(instructions)
        
        agent = self.coordinator.factory.create_agent(name, role, instruction_text)
        print(f"✅ Created agent: {name}")
    
    def _query_agent(self, command):
        """Query a specific agent"""
        parts = command.split(" ", 2)
        if len(parts) < 3:
            print("Usage: query <agent_name> <question>")
            return
        
        agent_name = parts[1]
        question = parts[2]
        
        agent = self.coordinator.factory.get_agent(agent_name)
        if agent:
            print(f"\n🤖 {agent_name} responding...")
            response = agent.process_query(question)
            print(response)
            print()
        else:
            print(f"Agent '{agent_name}' not found.")
    
    def _run_workflow(self, command):
        """Run an agent workflow"""
        parts = command.split(" ", 2)
        if len(parts) < 3:
            print("Usage: workflow <workflow_name> <query>")
            print("Available workflows: intel_to_strategy, research_deep_dive")
            return
        
        workflow_name = parts[1]
        query = parts[2]
        
        print(f"\n🔄 Running workflow: {workflow_name}")
        result = self.coordinator.run_agent_workflow(workflow_name, query)
        
        for key, value in result.items():
            print(f"\n{key.upper()}:")
            print(value)
        print()

if __name__ == "__main__":
    cli = AgentCLI()
    cli.run()
