"""
conftest.py  --  setup that pytest reads automatically.

You will not run this file yourself. pytest finds it, reads it, and applies it
to every test in this folder. The name is fixed: it must be exactly conftest.py.

WHAT IT DOES HERE
The tests live in tests/, but the code they test lives one folder up. Python
does not search upward on its own, so this adds the project folder to the
search path. Without it, every test would fail with ModuleNotFoundError before
running a single check.
"""

import os
import sys

# The folder containing this file (tests/), then its parent (the project root).
TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(TESTS_DIR)

# Insert at position 0 so our own files are found before anything else with a
# matching name.
sys.path.insert(0, PROJECT_ROOT)
