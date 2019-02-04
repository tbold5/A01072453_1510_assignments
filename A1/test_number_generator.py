from unittest import TestCase
from lotto import number_generator
import random

class TestNumber_generator(TestCase):
    def test_number_generator_normal(self):
        random.seed(1)
        expected = [5, 8, 9, 17, 32, 37]
        actual = number_generator()
        self.assertEqual(actual, expected)

    def test_number_generator_length(self):
        random.seed(1)
        expected = 6
        actual = len(number_generator())
        self.assertEqual(actual, expected)

    def test_number_generator_type(self):
        expected = list
        actual = type(number_generator())
        self.assertEqual(actual, expected)
