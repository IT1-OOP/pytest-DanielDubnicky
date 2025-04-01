import pytest
from src import calculator

def test_add():
    assert calculator.add(5,3) == 8

def test_add_wrong():
    assert calculator.add_wrong(5,3) == 8

def test_subtract():
    assert calculator.subtract(5,3) == 2

def test_multiply():
    assert calculator.multiply(5,3) == 15

def test_multiply_wrong():
    assert calculator.multiply_wrong(5.3) == 15

def test_divide():
    assert calculator.divide(6,2) == 3
    
def test_quadratic_formula():
    assert calculator.solve_quadratic_formula(1, 2, 1) == (-1.0, -1.0)
    assert calculator.solve_quadratic_formula(5, 2, 15) == (-1.0,-5.34)
    assert calculator.solve_quadratic_formula(0, 2, 15) == (-2.1, -6.2)