from unittest import TestCase
from roman_numbers import convert_to_roman_numeral


class TestConvert_to_roman_numeral(TestCase):
    def test_convert_to_roman_numeral_normal(self):
        expected = 'X'
        actual = convert_to_roman_numeral(10)
        self.assertEqual(actual, expected)

    def test_convert_to_roman_numeral_length(self):
        expected = 18
        actual = len(convert_to_roman_numeral(8898))
        self.assertEqual(actual, expected)

    def test_convert_to_roman_numeral_type(self):
        expected = str
        actual = type(convert_to_roman_numeral(8898))
        self.assertEqual(actual, expected)
