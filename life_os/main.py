
#!/usr/bin/env python3
"""
Life OS - Personal Life Management Company
Three Branch System: Intel, Directional, Executive
With Financial, Social, Political, Psychological, Physiological Wings
"""

import time
import schedule
from pathlib import Path
from datetime import datetime

# Import the three main branches
from branches.intel_branch import IntelBranch
from branches.directional_branch import DirectionalBranch  
from branches.executive_branch import ExecutiveBranch

# Import wings (departments)
from wings.financial_wing import FinancialWing
from wings.social_wing import SocialWing
from wings.political_wing import PoliticalWing
from wings.psychological_wing import PsychologicalWing
from wings.physiological_wing import PhysiologicalWing

# Import agent system
from agents.agent_coordinator import AgentCoordinator

class LifeOS:
    """
    Personal Life Management Company
    Automated execution mechanism for life optimization
    Based on Taleb's principles and game theory
    """
    
    def __init__(self):
        print("🚀 Initializing Life OS - Your Personal Management Company")
        print("=" * 60)
        
        # Initialize the three main branches
        self.intel_branch = IntelBranch()
        self.directional_branch = DirectionalBranch()
        self.executive_branch = ExecutiveBranch()
        
        # Initialize wings (departments)
        self.financial_wing = FinancialWing()
        self.social_wing = SocialWing()
        self.political_wing = PoliticalWing()
        self.psychological_wing = PsychologicalWing()
        self.physiological_wing = PhysiologicalWing()
        
        # Initialize agent coordination system
        self.agent_coordinator = AgentCoordinator()
        self.agents = self.agent_coordinator.setup_default_agents()
        
        # System state
        self.running = True
        self.current_worldview = {}
        self.active_protocols = []
        self.strategic_position = {}
        
        print("✅ Life OS initialized successfully")
        print("🤖 AI Agent network ready for custom instructions")
        
    def start_flywheel(self):
        """Start the main flywheel - set and forget operation"""
        print("\n🌀 Starting Life OS Flywheel...")
        print("📊 Intel → 🎯 Direction → ⚡ Execution → 📈 Compound")
        
        # Schedule continuous operations
        self._schedule_operations()
        
        # Start main loop
        while self.running:
            try:
                # Run scheduled operations
                schedule.run_pending()
                
                # Brief pause
                time.sleep(10)
                
            except KeyboardInterrupt:
                print("\n🛑 Life OS shutting down...")
                self.running = False
                break
    
    def _schedule_operations(self):
        """Schedule all automated operations"""
        # Intel gathering - continuous
        schedule.every(30).minutes.do(self._intel_sweep)
        
        # Strategic planning - daily
        schedule.every().day.at("06:00").do(self._strategic_planning)
        
        # Execution coordination - hourly
        schedule.every().hour.do(self._execution_coordination)
        
        # Wing operations - various frequencies
        schedule.every().hour.do(self.financial_wing.monitor)
        schedule.every(2).hours.do(self.social_wing.maintain_relationships)
        schedule.every().day.do(self.psychological_wing.wellness_check)
        schedule.every(4).hours.do(self.physiological_wing.health_monitor)
        
        print("⏰ All operations scheduled for automation")
    
    def _intel_sweep(self):
        """Intel branch gathers intelligence"""
        print("\n🔍 INTEL SWEEP INITIATED")
        intel_report = self.intel_branch.conduct_sweep()
        
        # Share intel with directional branch
        self.directional_branch.process_intel(intel_report)
        
        return intel_report
    
    def _strategic_planning(self):
        """Directional branch plans strategy"""
        print("\n🎯 STRATEGIC PLANNING SESSION")
        strategy = self.directional_branch.generate_strategy()
        
        # Send strategy to executive branch
        self.executive_branch.receive_strategy(strategy)
        
        return strategy
    
    def _execution_coordination(self):
        """Executive branch coordinates execution"""
        print("\n⚡ EXECUTION COORDINATION")
        execution_report = self.executive_branch.coordinate_execution()
        
        # Feed results back to intel for learning
        self.intel_branch.receive_feedback(execution_report)
        
        return execution_report
    
    def emergency_protocol(self, threat_type):
        """Emergency response protocol"""
        print(f"🚨 EMERGENCY PROTOCOL ACTIVATED: {threat_type}")
        
        # All branches coordinate emergency response
        intel_assessment = self.intel_branch.emergency_assessment(threat_type)
        strategic_response = self.directional_branch.emergency_strategy(intel_assessment)
        execution_plan = self.executive_branch.emergency_execution(strategic_response)
        
        return {
            "threat": threat_type,
            "assessment": intel_assessment,
            "strategy": strategic_response,
            "execution": execution_plan
        }
    
    def status_report(self):
        """Generate comprehensive status report"""
        return {
            "timestamp": datetime.now().isoformat(),
            "intel_status": self.intel_branch.get_status(),
            "directional_status": self.directional_branch.get_status(),
            "executive_status": self.executive_branch.get_status(),
            "wings_status": {
                "financial": self.financial_wing.get_status(),
                "social": self.social_wing.get_status(),
                "political": self.political_wing.get_status(),
                "psychological": self.psychological_wing.get_status(),
                "physiological": self.physiological_wing.get_status()
            }
        }

def main():
    """Main entry point"""
    life_os = LifeOS()
    
    # Start the automated flywheel
    life_os.start_flywheel()

if __name__ == "__main__":
    main()
