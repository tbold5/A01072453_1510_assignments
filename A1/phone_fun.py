def number_translator():
    """Translates alphabetical numbers

    A function that translates alphabetical numbers into numerical quivalent.
    PRECONDITION: promt user to input 10 character telephone number in the format XXX-XXX-XXXX
    POSTCONDITION: translate alphabetical numbers into numerical equivalents.
    RETURN: returns string in the format below.

    """

    user_input = input("Please enter 10-character phone number in the format XXX-XXX-XXXX: ").upper()
    new_number = str(letter_translator(user_input[0])) + str(letter_translator(user_input[1])) \
                 + str(letter_translator(user_input[2])) + str(letter_translator(user_input[3])) \
                 + str(letter_translator(user_input[4])) + str(letter_translator(user_input[5])) \
                 + str(letter_translator(user_input[6])) + str(letter_translator(user_input[7])) \
                 + str(letter_translator(user_input[8])) + str(letter_translator(user_input[9])) \
                 + str(letter_translator(user_input[10])) + str(letter_translator(user_input[11]))
    return new_number

def letter_translator(letter):
    list = [["0"],
            ["1"],
            ["2", "A", "B", "C"],
            ["3", "D", "E", "F"],
            ["4", "G", "H", "I"],
            ["5", "J", "K", "L"],
            ["6", "M", "N", "O"],
            ["7", "P", "Q", "R", "S"],
            ["8", "T", "U", "V"],
            ["9", "W", "X", "Y", "Z"],
            ["-"]]
    if letter in list[0]:
        return "0"
    elif letter in list[1]:
        return "1"
    elif letter in list[2]:
        return "2"
    elif letter in list[3]:
        return "3"
    elif letter in list[4]:
        return "4"
    elif letter in list[5]:
        return "5"
    elif letter in list[6]:
        return "6"
    elif letter in list[7]:
        return "7"
    elif letter in list[8]:
        return "8"
    elif letter in list[9]:
        return "9"
    elif letter in list[10]:
        return "-"

def main():
    print((number_translator()))

if __name__ == "__main__":
    main()