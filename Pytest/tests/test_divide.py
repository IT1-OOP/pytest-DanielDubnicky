import pytest
from src import calculator

def test_divide():
    assert calculator.divide(6,2) == 3