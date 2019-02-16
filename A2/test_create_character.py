from unittest import TestCase
from dungeonsanddragons import create_character
from unittest.mock import patch
import random


class TestCreate_character(TestCase):
    @patch('builtins.input', return_value='1')
    @patch('dungeonsanddragons.class_creator', return_value='monk')
    def test_create_character_negative(self, mock_class, mock_inventory):
        expected = None
        actual = create_character(-1)
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='1')
    @patch('dungeonsanddragons.class_creator', return_value='monk')
    def test_create_character_type(self, mock_class, mock_inventory):
        expected = dict
        actual = type(create_character(1))
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='1')
    @patch('dungeonsanddragons.class_creator', return_value='monk')
    def test_create_character_user_input(self, mock_class, mock_inventory):
        random.seed(1)
        expected = {'Charisma': 6,
                    'Class': 'monk',
                    'Constitution': 18,
                    'Dexterity': 17,
                    'HP': 2,
                    'Intelligence': 15,
                    'Inventory': ['Shield'],
                    'Name': 'Gudi',
                    'Strength': 18,
                    'Wisdom': 9,
                    'XP': 0}
        actual = create_character(2)
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='1')
    @patch('dungeonsanddragons.class_creator', return_value='monk')
    def test_create_character_length(self, mock_class, mock_inventory):
        expected = 11
        actual = len(create_character(2))
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='1')
    @patch('dungeonsanddragons.class_creator', return_value='monk')
    def test_create_character_name_length(self, mock_class, mock_inventory):
        expected = 4
        actual = len(create_character(2)['Name'])
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='4')
    @patch('dungeonsanddragons.class_creator', return_value='monk')
    def test_create_character_inventory_length(self, mock_class, mock_inventory):
        expected = 4
        actual = len(create_character(2)['Inventory'])
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='4')
    @patch('dungeonsanddragons.class_creator', return_value='monk')
    def test_create_character_HP_check(self, mock_class, mock_inventory):
        self.assertTrue(create_character(2)['HP'], )
