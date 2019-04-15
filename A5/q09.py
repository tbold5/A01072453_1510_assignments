"""COMP1510 Assignment 5: Back to basics"""

# Trae Bold
# A01072453
# JAN 11, 2019

import doctest


def base_conversion(original_base: int, original_number: int, destination_base: int) -> int:
    """Do base conversion.

    A function that converts any number with base between 2 - 10 to destination base of choice between 2 - 10.
    PRECONDITION: original_base must be an integer between 2- 10.
    PRECONDITION: destination_base must be an integer between 2 - 10.
    RETURN: new value as an integer.
    >>> base_conversion(2, 110001110, 10)
    398
    >>> base_conversion(10, 36, 2)
    100100
    """
    for num in str(original_number):
        if int(num) >= original_base:
            raise ValueError('\nOriginal number can not contain digit greater than or equal to base!\n')
    final = ''
    decimal = 0
    number_list = []
    number_length = len(str(original_number))

    for number in str(original_number):
        number_list.append(number)

    # Turn any number into decimal number.
    for i in range(number_length):
        number_length -= 1
        decimal += (int(number_list[i]) * (original_base ** number_length))

    # Integer division until decimal equals to 0.
    while decimal != 0:
        final += str(decimal % destination_base)
        decimal = decimal // destination_base

    # Reverse the string and return it as an integer.
    return int(final[::-1])


def main():
    try:
        print(base_conversion(2, 110001110, 10))
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
