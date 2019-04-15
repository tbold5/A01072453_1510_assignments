"""COMP1510 Assignment 5: Back to basics"""

# Trae Bold
# A01072453
# JAN 11, 2019

import doctest


def sum_of_primes(upper_bound: int) -> int:
    """Calculate sum_of_primes.

    A function that accepts a single positive integer and
    returns the sum of primes between 0 - upper_bound as an integer.
    PRECONDITION: upper_bound must be a positive integer.
    PARAM: upper_bound, a positive int
    RETURN: integer, sum of primes between 0 - upper_bound as an integer.
    >>> sum_of_primes(12)
    28
    >>> sum_of_primes(0)
    0
    """
    if upper_bound < 0:
        raise ValueError("Only positive integers accepted as upper bounds!")
    else:
        prime_list = []
        for num in range(2, upper_bound + 1):
            # Prime numbers are greater than 1
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    prime_list.append(num)
        return sum(prime_list)


def main():
    try:
        print(sum_of_primes(12))
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
