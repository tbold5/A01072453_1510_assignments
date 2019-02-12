from unittest import TestCase
from dungeonsanddragons import class_dictionary
import random

class TestClass_dictionary(TestCase):
    def test_class_dictionary_print(self):
        expected = {'barbarian': 12,
                    'bard': 8,
                    'blood Hunter': 10,
                    'cleric': 8,
                    'druid': 8,
                    'fighter': 10,
                    'monk': 8,
                    'paladin': 10,
                    'ranger': 10,
                    'rogue': 8,
                    'sorcerer': 6,
                    'warlock': 8,
                    'wizard': 6}
        actual = class_dictionary()
        self.assertEqual(expected, actual)

    def test_class_dictionary_type(self):
        expected = dict
        actual = type(class_dictionary())
        self.assertEqual(expected, actual)