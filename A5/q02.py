"""COMP1510 Assignment 5: Back to basics"""

# Trae Bold
# A01072453
# JAN 11, 2019

import doctest


def the_gcd(a, b: int) -> int:
    """Find greatest common divisor.

    A function that finds greatest common divisor between two integers.
    PRECONDITION: a, has to be non-zero integer.
    PRECONDITION: b, has to be non-zero integer.
    PARAM: a, an int.
    PARAM: b, an int.
    RETURN: int, greatest common divisor between a and b.
    >>> the_gcd(10, -25)
    5
    >>> the_gcd(11, -3)
    1
    """
    if a == 0 and b == 0:
        raise ValueError('Values has to be non-zero integers!')
    while b != 0:
        (a, b) = (b, a % b)
    # Return absolute value.
    return abs(a)


def main():
    try:
        print(the_gcd(0, 0))
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
