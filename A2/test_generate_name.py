from unittest import TestCase
from dungeonsanddragons import generate_name
import random


class TestGenerate_name(TestCase):
    def test_generate_name_value_error(self):
        self.assertRaises(ValueError)
        generate_name(-1)

    def test_generate_name_type(self):
        expected = str
        actual = type(generate_name(1))
        self.assertEqual(expected, actual)

    def test_generate_name_constant_followed_vowel(self):
        random.seed(1)
        syllable = generate_name(1)
        self.assertNotIn(syllable[0], syllable[1])
