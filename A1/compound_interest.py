"""COMP 1510 Assignment 1: Compound Interest calculator!"""

# Trae Bold
# A01072453
# Feb 03, 2019

import doctest


def compound_interest(p, r, n, t):
    """Calculate earned compound interest.

    A function that calculates the balance using compound interest formula.
    PARAM: P: amount originally deposited into the account.
        r: annual interest rate.
        n: number of times per year interest compounded.
        t: number of years the account will be left alone to grow.
    PRECONDITION: P must be a float.
        r must be a float.
        n must be an int and can not be a 0.
        t is an int.
    RETURN: float, the correct amount money in the account after elapsed time.

    >>> compound_interest(10, 3, 2, 2)
    390.625
    >>> compound_interest(-1, -1, -1, -1)
    -2.0
    >>> compound_interest(0, 0, 5, 0)
    0.0
    """

    total_amount = float(p) * (1 + (float(r) / int(n))) ** int(n * t)
    return total_amount


def main():
    print(compound_interest(1, 1, 1, 1))


if __name__ == "__main__":
    main()
    doctest.testmod()
