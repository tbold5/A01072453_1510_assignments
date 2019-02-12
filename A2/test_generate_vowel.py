from unittest import TestCase
from dungeonsanddragons import generate_vowel
import random


class TestGenerate_vowel(TestCase):
    def test_generate_vowel_output(self):
        random.seed(1)
        expected = 'e'
        actual = generate_vowel()
        self.assertEqual(expected, actual)

    def test_generate_vowel_length(self):
        expected = 1
        actual = len(generate_vowel())
        self.assertEqual(expected, actual)

    def test_generate_vowel_type(self):
        expected = str
        actual = type(generate_vowel())
        self.assertEqual(expected, actual)