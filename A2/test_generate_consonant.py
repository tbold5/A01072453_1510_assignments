from unittest import TestCase
from dungeonsanddragons import generate_consonant
import random


class TestGenerate_consonant(TestCase):
    def test_generate_consonant_output(self):
        random.seed(1)
        expected = 'g'
        actual = generate_consonant()
        self.assertEqual(expected, actual)

    def test_generate_consonant_length(self):
        expected = 1
        actual = len(generate_consonant())
        self.assertEqual(expected, actual)

    def test_generate_consonant_type(self):
        expected = str
        actual = type(generate_consonant())
        self.assertEqual(expected, actual)
