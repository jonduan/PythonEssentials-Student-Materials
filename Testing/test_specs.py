# test_specs.py
"""Python Essentials: Testing.
<Name>
<Class>
<Date>
"""

import specs
import pytest

# Problem 1: Test the addition and smallest factor functions from specs.py
def test_addition():
    pass

def test_smallest_factor():
    pass

# Problem 2: Test the operator function from specs.py
def test_operator():
    pass

# Problem 3: Finish testing the complex number class
@pytest.fixture
def set_up_complex_nums():
    number_1 = specs.ComplexNumber(1, 2)
    number_2 = specs.ComplexNumber(5, 5)
    number_3 = specs.ComplexNumber(2, 9)
    return number_1, number_2, number_3

def test_complex_addition(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 + number_2 == specs.ComplexNumber(6, 7)
    assert number_1 + number_3 == specs.ComplexNumber(3, 11)
    assert number_2 + number_3 == specs.ComplexNumber(7, 14)
    assert number_3 + number_3 == specs.ComplexNumber(4, 18)

def test_complex_multiplication(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 * number_2 == specs.ComplexNumber(-5, 15)
    assert number_1 * number_3 == specs.ComplexNumber(-16, 13)
    assert number_2 * number_3 == specs.ComplexNumber(-35, 55)
    assert number_3 * number_3 == specs.ComplexNumber(-77, 36)

# Problem 4: Write test cases for the Set game.
