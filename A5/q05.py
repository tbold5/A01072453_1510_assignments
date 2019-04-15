"""COMP1510 Assignment 5: Back to basics"""

# Trae Bold
# A01072453
# JAN 11, 2019

import doctest


def cashmoney(double: float) -> dict:
    """Represent each bill.

    A function that takes double that represents amount of Canadian money,
    and determines fewest of each bill and coin we need to represent it.
    PRECONDITION: double must be a positive float.
    PARAM: double, a float.
    RETURN: dictionary, that stores values to represent each bill needed to represent the money.
    >>> cashmoney(532.54)
    {100: 5, 50: 0, 20: 1, 10: 1, 5: 0, 2: 1, 1: 0, 0.25: 2, 0.1: 0, 0.05: 0, 0.01: 3}
    >>> cashmoney(0)
    {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.1: 0, 0.05: 0, 0.01: 0}
    """
    if double < 0:
        raise ValueError('Double must be a positive number!')
    else:
        denominations = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}
        for bill in denominations.keys():
            if denominations[bill] >= 0:
                denominations[bill] += int(double // bill)
                double -= denominations[bill] * bill
        return denominations


def main():
    try:
        print(cashmoney(532.54))
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
