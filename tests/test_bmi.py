import unittest
from bmi import calculate_bmi

class TestBMI(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(calculate_bmi(70, 1.75), 22.86)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            calculate_bmi(70, 0)

if __name__ == '__main__':
    unittest.main()
