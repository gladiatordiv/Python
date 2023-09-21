import pytest
def add(a, b):
    return a + b
@pytest.fixture
def setup_numbers():
    num1 = 5
    num2 = 3
    yield num1, num2 
def positive_numbers(setup_numbers):
    num1, num2 = setup_numbers
    result = add(num1, num2)
    assert result == 8  
def negative_numbers():
    result = add(-2, -3)
    assert result == -5 
