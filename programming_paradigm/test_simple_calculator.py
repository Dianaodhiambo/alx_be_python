import unittest
import importlib

# Define the SimpleCalculator class
class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""

    def add(self, a, b):
        """Return the addition of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the subtraction of b from a."""
        return a - b

    def multiply(self, a, b):
        """Return the multiplication of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the division of a by b. Returns None if b is zero."""
        if b == 0:
            return None
        return a / b

# Create a dummy module to simulate the import
import sys
import types

# Create a module object and add the SimpleCalculator class to it
module = types.ModuleType("simple_calculator")
sys.modules["simple_calculator"] = module
module.SimpleCalculator = SimpleCalculator

# Now we perform the import
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(2, 3), 5, "Addition test failed")
        self.assertEqual(self.calc.add(-1, 1), 0, "Addition test failed")
        self.assertEqual(self.calc.add(0, 0), 0, "Addition test failed")
        self.assertEqual(self.calc.add(-1, -1), -2, "Addition test failed")

    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(3, 2), 1, "Subtraction test failed")
        self.assertEqual(self.calc.subtract(1, 1), 0, "Subtraction test failed")
        self.assertEqual(self.calc.subtract(0, 0), 0, "Subtraction test failed")
        self.assertEqual(self.calc.subtract(-1, -1), 0, "Subtraction test failed")
        self.assertEqual(self.calc.subtract(1, -1), 2, "Subtraction test failed")

    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(2, 3), 6, "Multiplication test failed")
        self.assertEqual(self.calc.multiply(-1, 1), -1, "Multiplication test failed")
        self.assertEqual(self.calc.multiply(0, 10), 0, "Multiplication test failed")
        self.assertEqual(self.calc.multiply(-1, -1), 1, "Multiplication test failed")

    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(6, 3), 2, "Division test failed")
        self.assertEqual(self.calc.divide(-6, 3), -2, "Division test failed")
        self.assertEqual(self.calc.divide(0, 1), 0, "Division test failed")
        self.assertEqual(self.calc.divide(1, -1), -1, "Division test failed")
        self.assertIsNone(self.calc.divide(1, 0), "Division by zero test failed")

if __name__ == "__main__":
    unittest.main()



