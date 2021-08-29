import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/../")
"""
Write your module
Ex. import hoge
"""
from batch import mainCmd  # noqa: E402


def test_is_mainCmd():
    assert mainCmd() == "Hello, Python Batch!"
