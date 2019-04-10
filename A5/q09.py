"""COMP1510 Assignment 5: Back to basics"""

# Trae Bold
# A01072453
# JAN 11, 2019


def base_conversion(original_base: int, original_number: int, destination_base: int) -> int:
    """Converts base 10 into base b. . Each time a division is performed the remainder and quotient are saved.
    At each step, the dividend (numerator) is the quotient from the preceding step; the divisor (denominator) is always b.
    """

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
    print(base_conversion(10, 16, 2))


if __name__ == '__main__':
    main()
