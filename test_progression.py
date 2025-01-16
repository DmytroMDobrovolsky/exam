import unittest
from progression import sum_arithmetic_progression

class TestArithmeticProgression(unittest.TestCase):
    def test_sum_positive(self):
        self.assertEqual(sum_arithmetic_progression(5), 30.0)
        self.assertEqual(sum_arithmetic_progression(10), 110.0)

    def test_sum_one(self):
        self.assertEqual(sum_arithmetic_progression(1), 2.0)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            sum_arithmetic_progression(0)
        with self.assertRaises(ValueError):
            sum_arithmetic_progression(-5)

if __name__ == "__main__":
    unittest.main()
