from unittest import TestCase
from dungeonsanddragons import generate_syllable
import random

class TestGenerate_syllable(TestCase):
    def test_generate_syllable_output(self):
        random.seed(1)
        expected = 'gu'
        actual = generate_syllable()
        self.assertEqual(expected, actual)

    def test_generate_syllable_length(self):
        expected = 2
        actual = len(generate_syllable())
        self.assertEqual(expected, actual)

    def test_generate_syllable_type(self):
        expected = str
        actual = type(generate_syllable())
        self.assertEqual(expected, actual)

    def test_generate_syllable_consonant_followed_vowel(self):
        random.seed(1)
        syllable = generate_syllable()
        self.assertNotIn(syllable[0], syllable[1])
