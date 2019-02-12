from unittest import TestCase
from dungeonsanddragons import class_creator
import random
from unittest.mock import patch


class TestClass_creator(TestCase):
    @patch('dungeonsanddragons.class_creator', return_value='paladin')
    def test_class_creator_print(self, mock_class):
        expected = 'paladin'
        actual = class_creator()
        self.assertEqual(expected, actual)
    @patch('dungeonsanddragons.class_creator', return_value='orc')
    def test_class_creator_not_in(self, mock_class):
        expected = 'Please Choose Character Class from the list!'
        actual = class_creator()
        self.assertEqual(expected, actual)
