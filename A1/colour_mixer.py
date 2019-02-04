"""COMP 1510 Assignment 1: Colour Mixer!"""

# Trae Bold
# A01072453
# Feb 03, 2019

import doctest


def colour_mixer():
    """Generate a secondary colour.

    A function that takes two primary colours and generates new secondary colour.
    PARAM: N/A
    PRECONDITION: string must be a primary colour: Red, Yellow or Blue.
    POSTCONDITION: string, prints the correct secondary colour and correct error message.
    """
    chosen_colour_1 = input("Please choose first primary colour from RED, YELLOW or BLUE: ")
    chosen_colour_2 = input("Please choose second primary colour from RED, YELLOW or BLUE: ")

    strip_colour_1 = chosen_colour_1.strip()
    strip_colour_2 = chosen_colour_2.strip()

    input_colour_1 = strip_colour_1.lower()
    input_colour_2 = strip_colour_2.lower()

    colour_checker(input_colour_1, input_colour_2)

    # Use "or" inside if else statement to get rid of input order problem.


def colour_checker(input_colour_1, input_colour_2):
    """Check colour mixes.

    A function that checks two colours and prints new colour accordingly.
    PARAM: string, from 'red' or 'yellow' or 'blue'.
    PRECONDITION: user must choose from the give three primary colours 'red', 'blue', 'yellow'.
    POSTCONDITION: must print secondary colour by checking two given parameters or print helpful error messages.

    >>> colour_checker('red', 'blue')
    The secondary colour is: Purple
    >>> colour_checker('blue', 'blue')
    You entered two same colours
    >>> colour_checker('pink', 'black')
    You did not pick a primary colour
    """
    if input_colour_1 == "red" and input_colour_2 == "blue" \
            or input_colour_1 == "blue" and input_colour_2 == "red":
            print("The secondary colour is: Purple")
    elif input_colour_1 == "red" and input_colour_2 == "yellow" \
            or input_colour_1 == "yellow" and input_colour_2 == "red":
            print("The secondary colour is: Orange")
    elif input_colour_1 == "yellow" and input_colour_2 == "blue" \
            or input_colour_1 == "blue" and input_colour_2 == "yellow":
            print("The secondary colour is: Green")
    elif input_colour_1 == input_colour_2:
        print("You entered two same colours")
    else:
        print("You did not pick a primary colour")


def main():
    colour_mixer()
    doctest.testmod()


if __name__ == "__main__":
    main()
