"""COMP 1510 Assignment 1: Seconds converter!"""

# Trae Bold
# A01072453
# Feb 03, 2019
import doctest


def time_calculator(seconds):
    """Convert seconds.

    A function that converts seconds to day, hours, minutes, and seconds.
    PARAM: int, seconds.
    PRE: number must be a positive integer.
    RETURN: returns number of days, hours, minutes and seconds as integer in a list.

    >>> time_calculator(61)
    [0, 0, 1, 1]
    >>> time_calculator(2019)
    [0, 0, 33, 39]
    >>> time_calculator(360709)
    [4, 4, 11, 49]
    """

    my_calculator = []
    my_calculator.append(seconds // 86400)
    hours = seconds % 86400
    my_calculator.append(hours // 3600)
    minutes = hours % 3600
    my_calculator.append(minutes // 60)
    seconds = minutes % 60
    my_calculator.append(seconds)

    return my_calculator


def main():
    print(time_calculator())


if __name__ == "__main__":
    main()
    doctest.testmod()

