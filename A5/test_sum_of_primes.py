from unittest import TestCase
from q01 import sum_of_primes


class TestSumOfPrimes(TestCase):
    def test_sum_of_primes_type(self):
        self.assertEqual(int, type(sum_of_primes(11)))

    def test_sum_of_primes_zero(self):
        self.assertEqual(0, sum_of_primes(0))

    def test_sum_of_primes_negative(self):
        with self.assertRaises(ValueError):
            sum_of_primes(-1)

    def test_sum_of_primes_success(self):
        self.assertEqual(10, sum_of_primes(5))
