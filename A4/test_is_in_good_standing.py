from unittest import TestCase
from crud import is_in_good_standing


class TestIsInGoodStanding(TestCase):
    def test_is_in_good_standing_true(self):
        expected = True
        actual = is_in_good_standing('1')
        self.assertEqual(expected, actual)

    def test_is_in_good_standing_false(self):
        expected = False
        actual = is_in_good_standing('2')
        self.assertEqual(expected, actual)

    def test_is_in_good_standing_none(self):
        expected = None
        actual = is_in_good_standing('3')
        self.assertEqual(expected, actual)

    def test_is_in_good_standing_type(self):
        expected = bool
        actual = type(is_in_good_standing('1'))
        self.assertEqual(expected, actual)
