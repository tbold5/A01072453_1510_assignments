from unittest import TestCase
from dungeonsanddragons import print_character
import random
from unittest.mock import patch


class TestPrint_character(TestCase):
    @patch('dungeonsanddragons.choose_inventory', return_value=['Elixir'])
    @patch('dungeonsanddragons.class_creator', return_value='monk')
    def test_print_character_output(self, mock_class, mock_inventory):
        expected = {'Charisma': 15,
                    'Class': 'monk',
                    'Constitution': 18,
                    'Dexterity': 6,
                    'HP': 10,
                    'Intelligence': 17,
                    'Inventory': ['Elixir'],
                    'Name': 'Gu',
                    'Strength': 11,
                    'Wisdom': 18,
                    'XP': 0}
        random.seed(1)
        actual = print_character(1)
        self.assertEqual(expected, actual)

    def test_print_character_type(self):
            expected = dict
            actual = type(print_character(1))
            self.assertEqual(expected, actual)
