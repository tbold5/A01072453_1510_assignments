def number_translator():
    """Translates alphabetical numbers

    A function that translates alphabetical numbers into numerical quivalent.
    PRE: promt user to input 10 character telephone number in the format XXX-XXX-XXXX
    POST: translate alphabetical numbers into numerical equivalents.
    RETURN: returns string in the format below.

    """

    initial_input = input("Please enter 10-character phone number in the format XXX-XXX-XXXX: ")
    space_input = initial_input.strip()
    upper_input = space_input.lower()
    





def main():
    print((number_translator()))

if __name__ == "__main__":
    main()