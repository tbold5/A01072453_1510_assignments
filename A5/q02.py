"""COMP1510 Assignment 5: Back to basics"""

# Trae Bold
# A01072453
# JAN 11, 2019


def the_gcd(a, b: int) -> int:
    while b != 0:
        (a, b) = (b, a % b)
    # Return absolute value.
    return abs(a)


def main():
    print(the_gcd(10, -25))


if __name__=='__main__':
    main()
