"""
Example Calculator Module

This is a sample module to demonstrate the autonomous test generation and review workflow.
"""


class Calculator:
    """A simple calculator class for demonstration"""

    def __init__(self):
        self.last_result = None

    def add(self, a: float, b: float) -> float:
        """Add two numbers"""
        result = a + b
        self.last_result = result
        return result

    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a"""
        result = a - b
        self.last_result = result
        return result

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers"""
        result = a * b
        self.last_result = result
        return result

    def divide(self, a: float, b: float) -> float:
        """Divide a by b"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.last_result = result
        return result

    def get_last_result(self) -> float:
        """Get the last calculated result"""
        return self.last_result


def factorial(n: int) -> int:
    """Calculate factorial of n"""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def is_prime(n: int) -> bool:
    """Check if a number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
