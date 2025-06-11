
#!/usr/bin/env python3
"""
Life OS - Main Entry Point
A sophisticated AI crew management system for life optimization
Based on Taleb's principles: Antifragility, Convexity, Asymmetric Opportunities
"""

import sys
from pathlib import Path

# Add life_os to Python path
sys.path.append(str(Path(__file__).parent / "life_os"))

from life_os.main import main

if __name__ == "__main__":
    main()
