"""COMP1510 Assignment # 3: Your First SUD!"""

# Trae Bold
# A01072453
# JAN 11, 2019

import random


def roll_die(number_of_rolls, number_of_sides):
    """Roll a die.

    A function that simulates rolling die of the specified size and the number of times.
    PARAM: int, number_of_rolls.
    PARAM: int, number_of_sides.
    PRECONDITION: number_of_rolls must be a positive integer or the function returns 0.
    PRECONDITION: number_of_sides must be a positive integer or the function returns 0.
    RETURN: random total of number_of_rolls and random_of_sides.
    >>> random.seed(1)
    >>> roll_die(1, 6)
    2
    """

    result = random.randint(1 * number_of_rolls, number_of_sides * number_of_rolls)
    if number_of_rolls < 0 and number_of_sides < 0:
        return 0
    else:
        return result


def my_character():
    my_character_dic = {'HP': 10, 'Damage': roll_die(1, 6), 'x': 3, 'y': 0}
    my_character_dic['Name'] = input('Please choose a name for you Hello Kitty:  ').title()
    return my_character_dic


def move_character():


def main():
    print(my_character())


if __name__ == "__main__":
    main()
