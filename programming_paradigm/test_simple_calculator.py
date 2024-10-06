import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-2, 1), -1)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtract(self):
        """Test the subtraction operation."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_multiply(self):
        """Test the multiplication operation."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 10), 0)

    def test_divide(self):
        """Test the division operation."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, -2), 5)
        
        # Test division by zero
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(self, 0)
        

if __name__ == "__main__":
    unittest.main()

