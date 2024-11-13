"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:
    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 8 == calculator.multiply(4, 2)

    def test_division(self):
        assert 5 == calculator.divide(10, 2)
        assert "cannot divide with 0" == calculator.divide(5, 0)
