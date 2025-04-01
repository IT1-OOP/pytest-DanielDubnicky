import pytest
from src import calculator

def test_add():
    assert calculator.add(1,2) == 3
    assert calculator.add(0, 5) == 5
    assert calculator.add(-2,9) == 7
    assert calculator.add(5, -8) == -3

def test_add_2():
    assert calculator.add_wrong(1,2) == 3
    assert calculator.add_wrong(0, 5) == 5
    assert calculator.add_wrong(-2,9) == 7
    assert calculator.add_wrong(0, 0) == 0

@pytest.mark.parametrize(
    "a, b, exptected",
    [
        (1, 2, 3),
        (0, 5, 5),
        (-2, 9, 7),
        (5, -8, -3),
    ],
)

def test_add_parametrized(a, b, exptected):
    assert calculator.add(a, b) == exptected

def test_add_wrong_parametrized(a, b, exptected):
    assert calculator.add_wrong(a, b) == exptected

@pytest.mark.parametrize(
    "x, y, exptected",
    [
        (1, 2, 2),
        (0, 5, 0),
        (-2, 9, -18),
        (5, -8, -40),
    ],
)

def test_multiply_parametrized(x, y, exptected):
    assert calculator.multiply(x, y) == exptected

def test_multiply_wrong_parametrized(x, y, exptected):
    assert calculator.multiply_wrong(x, y) == exptected

@pytest.mark.parametrize(
    "c, d, exptected",
    [
        (2, 2, 1),
        (0, 5, 0),
        (6, 2, 3),
        (9, 3, 3),
    ],
)

def test_subtract_parametrized(c, d, exptected):
    assert calculator.subtract(c, d) == exptected