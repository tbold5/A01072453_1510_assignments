def convert_to_roman_numeral(positive_int):
    """Convert an integer to a Roman numeral

        A function to converts number to Roman numeral.
        PARAM: number, a positive integer
        PRECONDITION: number must be positive integer
        POSTCONDITION: converts roman numeral
        RETURN: Roman numeral as a string
    """
    numeral_I = 1
    numeral_V = 5
    numeral_X = 10
    numeral_L = 50
    numeral_C = 100
    numeral_D = 500
    numeral_M = 1000