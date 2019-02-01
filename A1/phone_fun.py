def number_translator():
    """Translates alphabetical numbers

    A function that translates alphabetical numbers into numerical quivalent.
    PRE: promt user to input 10 character telephone number in the format XXX-XXX-XXXX
    POST: translate alphabetical numbers into numerical equivalents.
    RETURN: returns string in the format below.

    """

    initial_input = input("Please enter 10-character phone number in the format XXX-XXX-XXXX: ")
    space_input = initial_input.strip()
    upper_input = space_input.upper()
    empty_list = []

    if initial_input == "A" or upper_input == "B" or upper_input == "C" or upper_input == "2":
        empty_list.append("2")
    elif upper_input == "D" or upper_input == "E" or upper_input == "F" or upper_input == "3":
        empty_list.append("3")
    elif upper_input == "G" or upper_input == "H" or upper_input == "I" or upper_input == "4":
        empty_list.append("4")
    elif upper_input == "J" or upper_input == "K" or upper_input == "L" or upper_input == "5":
        empty_list.append("5")
    elif upper_input == "M" or upper_input == "N" or upper_input == "O" or upper_input == "6":
        empty_list.append("6")
    elif upper_input == "P" or upper_input == "Q" or upper_input == "R" or upper_input == "7":
        empty_list.append("7")
    elif upper_input == "T" or upper_input == "U" or upper_input == "V" or upper_input =="8":
        empty_list.append("8")
    elif upper_input == "W" or upper_input == "X" or upper_input == "Y"\
            or upper_input == "Z" or upper_input == "9":
        empty_list.append("9")
    elif upper_input == "1":
        empty_list.append("1")

    #Another function that converts the whole string.

    return empty_list


def main():
    print((number_translator()))

if __name__ == "__main__":
    main()