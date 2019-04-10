"""COMP1510 Assignment 5: Back to basics"""

# Trae Bold
# A01072453
# JAN 11, 2019


def cashmoney(double: float) -> dict:
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
        print(cashmoney(-1))
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
