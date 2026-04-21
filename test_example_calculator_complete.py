"""
Complete test implementation example
This shows what the tests should look like after you implement them
"""

import pytest
from example_calculator import Calculator, factorial, is_prime


# Function Tests - factorial
def test_factorial_basic():
    """Test basic functionality of factorial"""
    assert factorial(5) == 120
    assert factorial(3) == 6
    assert factorial(1) == 1
    assert factorial(0) == 1


def test_factorial_edge_cases():
    """Test edge cases for factorial"""
    # Boundary conditions
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(10) == 3628800


def test_factorial_error_handling():
    """Test error handling in factorial"""
    # Negative numbers should raise ValueError
    with pytest.raises(ValueError, match="Factorial not defined for negative numbers"):
        factorial(-1)

    with pytest.raises(ValueError):
        factorial(-5)


# Function Tests - is_prime
def test_is_prime_basic():
    """Test basic functionality of is_prime"""
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True


def test_is_prime_edge_cases():
    """Test edge cases for is_prime"""
    # Non-prime numbers
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(9) == False

    # Large primes
    assert is_prime(97) == True
    assert is_prime(100) == False


def test_is_prime_error_handling():
    """Test error handling in is_prime"""
    # Negative numbers
    assert is_prime(-5) == False
    assert is_prime(-1) == False


# Class Tests - Calculator
class TestCalculatorIntegration:
    """Integration tests for Calculator"""

    def setup_method(self):
        """Setup test fixtures"""
        self.calc = Calculator()

    def test_add_basic(self):
        """Test basic add functionality"""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(10, 5) == 15
        assert self.calc.add(-1, 1) == 0

    def test_add_edge_cases(self):
        """Test edge cases for add"""
        assert self.calc.add(0, 0) == 0
        assert self.calc.add(-5, -5) == -10
        assert self.calc.add(1.5, 2.5) == 4.0

    def test_subtract_basic(self):
        """Test basic subtract functionality"""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(10, 5) == 5
        assert self.calc.subtract(0, 0) == 0

    def test_subtract_edge_cases(self):
        """Test edge cases for subtract"""
        assert self.calc.subtract(3, 5) == -2
        assert self.calc.subtract(-5, -3) == -2
        assert self.calc.subtract(0, 10) == -10

    def test_multiply_basic(self):
        """Test basic multiply functionality"""
        assert self.calc.multiply(2, 3) == 6
        assert self.calc.multiply(5, 5) == 25
        assert self.calc.multiply(10, 0) == 0

    def test_multiply_edge_cases(self):
        """Test edge cases for multiply"""
        assert self.calc.multiply(0, 100) == 0
        assert self.calc.multiply(-5, 3) == -15
        assert self.calc.multiply(-2, -2) == 4

    def test_divide_basic(self):
        """Test basic divide functionality"""
        assert self.calc.divide(6, 2) == 3
        assert self.calc.divide(10, 5) == 2
        assert self.calc.divide(7, 2) == 3.5

    def test_divide_edge_cases(self):
        """Test edge cases for divide"""
        assert self.calc.divide(0, 5) == 0
        assert self.calc.divide(-10, 2) == -5
        assert self.calc.divide(1, 3) == pytest.approx(0.333333, rel=1e-5)

    def test_divide_error_handling(self):
        """Test error handling in divide"""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(5, 0)

    def test_calculator_workflow(self):
        """Test complete workflow of Calculator"""
        # Test method interactions and state
        result1 = self.calc.add(10, 5)
        assert result1 == 15
        assert self.calc.get_last_result() == 15

        result2 = self.calc.multiply(result1, 2)
        assert result2 == 30
        assert self.calc.get_last_result() == 30

        result3 = self.calc.divide(result2, 3)
        assert result3 == 10
        assert self.calc.get_last_result() == 10

    def test_calculator_state_management(self):
        """Test state management across methods"""
        # Initial state
        assert self.calc.get_last_result() is None

        # State after operations
        self.calc.add(5, 5)
        assert self.calc.get_last_result() == 10

        self.calc.subtract(20, 5)
        assert self.calc.get_last_result() == 15

        self.calc.multiply(3, 4)
        assert self.calc.get_last_result() == 12


# Run tests with: pytest test_example_calculator_complete.py -v
