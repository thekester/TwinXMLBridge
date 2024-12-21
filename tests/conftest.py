# tests/conftest.py

import sys
from pathlib import Path

# Define the project's base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Add the base directory to sys.path
sys.path.append(str(BASE_DIR))
