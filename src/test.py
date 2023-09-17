
import unittest
from solution import calculate_factorial

class TestCalculateFactorial(unittest.TestCase):
    def test_factorial_of_zero(self):
        result = calculate_factorial(0)
        self.assertEqual(result, 1)

    def test_factorial_of_positive_number(self):
        result = calculate_factorial(5)
        self.assertEqual(result, 120)

    def test_factorial_of_large_number(self):
        result = calculate_factorial(10)
        self.assertEqual(result, 3628800)

if __name__ == '__main__':
    unittest.main()

