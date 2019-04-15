from unittest import TestCase
from q09 import base_conversion


class TestBase_conversion_type(TestCase):
    def test_base_conversion_type(self):
        self.assertEqual(int, type(base_conversion(2, 10, 10)))

    def test_base_conversion_error(self):
        with self.assertRaises(ValueError):
            base_conversion(2, 99, 10)

    def test_base_conversion_positive(self):
        self.assertEqual(2, base_conversion(2, 10, 10))

    def test_base_conversion_digit_to_binary(self):
        self.assertEqual(100100, base_conversion(10, 36, 2))

