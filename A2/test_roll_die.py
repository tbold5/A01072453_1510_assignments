from unittest import TestCase
from dungeonsanddragons import roll_die
import random


class TestRoll_die(TestCase):
    def test_roll_negative(self):
        expected = 0
        random.seed(1)
        actual = roll_die(-1, -1)
        self.assertEqual(expected, actual)

    def test_roll_equal(self):
        expected = 2
        random.seed(1)
        actual = roll_die(1, 6)
        self.assertEqual(expected, actual)

