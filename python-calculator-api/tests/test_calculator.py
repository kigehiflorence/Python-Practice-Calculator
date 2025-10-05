import pytest
from app.calculator import Calculator

def test_add():
    assert Calculator.add(2, 3) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        Calculator.divide(5, 0)
