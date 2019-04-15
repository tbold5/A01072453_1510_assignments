from unittest import TestCase
from q05 import cashmoney


class TestCashMoney(TestCase):

    def test_cashmoney_type(self):
        self.assertEqual(dict, type(cashmoney(11)))

    def test_cashmoney_correct(self):
        expected = {100: 5, 50: 0, 20: 1, 10: 1, 5: 0, 2: 1, 1: 0, 0.25: 2, 0.1: 0, 0.05: 0, 0.01: 3}
        actual = cashmoney(532.54)
        self.assertEqual(expected, actual)

    def test_cashmoney_length(self):
        self.assertTrue(len(cashmoney(1)) == 11)

    def test_cashmoney_negative(self):
        with self.assertRaises(ValueError):
            cashmoney(-99)

    def test_cashmoney_zero(self):
        expected = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.1: 0, 0.05: 0, 0.01: 0}
        actual = cashmoney(0)
        self.assertEqual(expected, actual)
