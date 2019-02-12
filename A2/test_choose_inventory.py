from unittest import TestCase
from dungeonsanddragons import choose_inventory
import random


class TestChoose_inventory(TestCase):
    def test_choose_empty_inventory(self):
        expected = []
        random.seed(1)
        actual = choose_inventory([], 0)
        self.assertEqual(expected, actual)

    def test_choose_inventory_length(self):
        expected = 2
        actual = len(choose_inventory(['Trae', 'Chris'], 2))
        self.assertEqual(expected, actual)

    def test_choose_inventory_equal(self):
        expected = ['Clarity', 'Hammer']
        random.seed(1)
        actual = choose_inventory(['Clarity', 'Hammer', 'Axe', 'Potion'], 2)
        self.assertEqual(actual, expected)
