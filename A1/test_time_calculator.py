from unittest import TestCase
from time_calculator import time_calculator

class TestTime_calculator(TestCase):
    def test_time_calculator_normal(self):
        expected = [0, 0, 1, 0]
        actual = time_calculator(60)
        self.assertEqual(actual, expected)

    def test_time_calculator_length(self):
        expected = 4
        actual = len(time_calculator(8998))
        self.assertEqual(actual, expected)

    def test_time_calculator_type(self):
        expected = list
        actual = type(time_calculator(135))
        self.assertEqual(actual, expected)
