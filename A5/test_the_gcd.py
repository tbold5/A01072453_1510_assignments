from unittest import TestCase
from q02 import the_gcd


class TestTheGcd(TestCase):
    def test_the_gcd_type(self):
        self.assertEqual(int, type(the_gcd(10, 5)))

    def test_the_gcd_is_absolute(self):
        self.assertTrue(the_gcd(15, -30) >= 0)

    def test_the_gcd_error(self):
        with self.assertRaises(ValueError):
            the_gcd(0, 0)

    def test_the_gcd_correct(self):
        self.assertEqual(5, the_gcd(10, -25))
