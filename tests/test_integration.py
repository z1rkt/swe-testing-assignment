import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from interface import calculate

def test_full_operation():
    result = calculate("+",5,3)
    assert result == 8

def test_clear_function():
    result = calculate("C",0)
    assert result == 0
