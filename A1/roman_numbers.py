"""COMP 1510 Assignment 1: Roman Converter!"""

# Trae Bold
# A01072453
# Feb 03, 2019

import doctest


def convert_to_roman_numeral(positive_int):
    """Convert an integer to a Roman numeral.

    A function to converts number to Roman numeral.
    PARAM: number, a positive integer.
    PRECONDITION: number must be positive integer in the range 1 - 10,000 and must not be 0.
    POSTCONDITION: converts roman numeral.
    RETURN: Roman numeral as a string.

    >>> convert_to_roman_numeral(2019)
    'MMXIX'
    >>> convert_to_roman_numeral(13)
    'XIII'
    >>> convert_to_roman_numeral(9639)
    'MMMMMMMMMDCXXXIX'
    """

    roman_numeral = ''
    # if positive_int == 0:
    #     print("nulla")
    if positive_int // 1000 > 0:
        roman_numeral += (positive_int // 1000) * "M"
        positive_int = positive_int % 1000
    if positive_int // 900 > 0:
        roman_numeral += (positive_int // 900) * "CM"
        positive_int = positive_int % 900
    if positive_int // 500 > 0:
        roman_numeral += (positive_int // 500) * "D"
        positive_int = positive_int % 500
    if positive_int // 400 > 0:
        roman_numeral += (positive_int // 400) * "CD"
        positive_int = positive_int % 400
    if positive_int // 100 > 0:
        roman_numeral += (positive_int // 100) * "C"
        positive_int = positive_int % 100
    if positive_int // 90 > 0:
        roman_numeral += (positive_int // 90) * "XL"
        positive_int = positive_int % 90
    if positive_int // 50 > 0:
        roman_numeral += (positive_int // 50) * "L"
        positive_int = positive_int % 50
    if positive_int // 40 > 0:
        roman_numeral += (positive_int // 40) * "XL"
        positive_int = positive_int % 40
    if positive_int // 10 > 0:
        roman_numeral += (positive_int // 10) * "X"
        positive_int = positive_int % 10
    if positive_int // 9 > 0:
        roman_numeral += (positive_int // 9) * "IX"
        positive_int = positive_int % 9
    if positive_int // 5 > 0:
        roman_numeral += (positive_int // 5) * "V"
        positive_int = positive_int % 5
    if positive_int // 4 > 0:
        roman_numeral += (positive_int // 4) * "IV"
        positive_int = positive_int % 4
    if positive_int // 1 > 0:
        roman_numeral += (positive_int // 1) * "I"
    return roman_numeral


def main():
    print(convert_to_roman_numeral(2019))


if __name__ == "__main__":
    main()
    doctest.testmod()
