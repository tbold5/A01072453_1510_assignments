from unittest import TestCase
from dungeonsanddragons import create_character
from unittest.mock import patch
import random


class TestCreate_character(TestCase):
    def test_create_character_none(self):
        expected = None
        actual = create_character(-1)
        self.assertEqual(expected, actual)

    @patch('dungeonsanddragons.choose_inventory', return_value='[Axe]')
    @patch('dungeonsanddragons.class_creator', return_value='monk')
    def test_create_character_user_input(self, mock_class, mock_inventory):
        random.seed(1)
        expected = {'Charisma': 6,
                    'Class': 'monk',
                    'Constitution': 18,
                    'Dexterity': 17,
                    'HP': 10,
                    'Intelligence': 15,
                    'Inventory': '[Axe]',
                    'Name': 'Gudi',
                    'Strength': 18,
                    'Wisdom': 9,
                    'XP': 0}
        actual = create_character(2)
        self.assertEqual(expected, actual)


