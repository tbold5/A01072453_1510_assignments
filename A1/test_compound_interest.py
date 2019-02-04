from unittest import TestCase
from compound_interest import compound_interest


class TestCompound_interest(TestCase):
    def test_compound_interest_normal(self):
        expected = 72570.6434401327
        actual = compound_interest(1, 3, 4, 5)
        self.assertEqual(actual, expected)

    def test_compound_interest_negative(self):
        expected = -2.0
        actual = compound_interest(-1, -1, -1, -1)
        self.assertEqual(actual, expected)

    def test_compound_interest_type(self):
        expected = float
        actual = type(compound_interest(1, 3, 5, 7))
        self.assertEqual(actual, expected)
