import pytest
from math_function import add

'''def test_add_positive_numbers():
    assert add(2,3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_mixed_numbers():
    assert add(2, -3) == -1

def test_add_zero():
    assert add(0,0) == 1'''

@pytest.mark.parametrize(
    "num1, num2, res",
    [(2,3,5), (-2,-3,-5), (2,-3,-1), (0,0,0)]
)
def test_add(num1, num2, res):
    assert add(num1,num2) == res

