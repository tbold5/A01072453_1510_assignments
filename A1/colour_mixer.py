def colour_mixer():
    """Generate a secondary colour

        A function that takes two primary colours and generates new secondary colour.
        PARAM: string, a primary colour
        PRE: string must be a primary colour: Red, Yellow or Blue
        POST: string, prints the correct secondary colour and correct error message.
    """
    chosen_colour_1 = input("Please choose first primary colour from RED, YELLOW or BLUE: ")
    chosen_colour_2 = input("Please choose first secondary colour from RED, YELLOW or BLUE: ")

    #Use "strip" method to get rid of useless whitespace.
    strip_colour_1 = chosen_colour_1.strip()
    strip_colour_2 = chosen_colour_2.strip()

    #Use "lower" method to turn any inputs to lowercase.
    input_colour_1 = strip_colour_1.lower()
    input_colour_2 = strip_colour_2.lower()

    #Use "or" inside if else statement to get rid of input order problem.
    if input_colour_1 == "red" and input_colour_2 == "blue" \
            or input_colour_1 == "blue" and input_colour_2 == "red":
            print("The secondary colour is: Purple")
    elif input_colour_1 == "red" and input_colour_2 == "yellow" \
            or input_colour_1 == "yellow" and input_colour_2 == "red":
            print("The secondary colour is: Orange")
    elif input_colour_1 == "yellow" and input_colour_2 == "blue" \
            or input_colour_1 == "blue" and input_colour_2 == "yellow":
            print("The secondary colour is: Green")
    else:
        print("You did not pick a primary colour, and you can not pick same two primary colours")


def main():
    colour_mixer()



if __name__ == "__main__":
    main()
