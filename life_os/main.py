
#!/usr/bin/env python3
"""
Life OS - Main Entry Point
A sophisticated AI crew management system for life optimization
"""

from crew import LifeOSCrew
import sys

def main():
    """Main entry point for Life OS"""
    print("🌟 Welcome to Life OS - Your AI-Powered Life Management System")
    print("=" * 60)
    
    try:
        # Initialize the Life OS crew
        life_crew = LifeOSCrew()
        
        # Start the crew operations
        life_crew.run()
        
    except KeyboardInterrupt:
        print("\n👋 Life OS shutting down gracefully...")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
