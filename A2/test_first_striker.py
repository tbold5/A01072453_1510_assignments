from unittest import TestCase
from dungeonsanddragons import first_striker
import random


class TestFirst_striker(TestCase):
    def test_first_striker_type(self):
        expected = bool
        actual = type(first_striker())
        self.assertEqual(expected, actual)

    def test_first_striker_evaluate(self):
        random.seed(1)
        opponent_1 = random.randint(1, 20)
        opponent_2 = random.randint(1, 20)
        expected = False
        actual = first_striker() == opponent_1 > opponent_2
        self.assertEqual(expected, actual)
