import random

def number_generator():
    """Number Generator

        A function that generates random 6 digit lottery number
        PRE: random numbers, between 1-49
        RETURN: in list from highest to lowest order
    """

    #Helper function get called in the main function without changing the header
    def helper_function(x):
        if x == 0:
            return []
        else:
            #add random integers from 1 - 49 to the list
            list = helper_function(x - 1)
            list.append(random.randint(1, 49))
            my_list = list
            my_list.sort()
            return my_list
    #Takes PARAM x and recurses until it reaches base condition x = 0


    #Prints the list by calling helper function that takes number of digits as parameter
    print(helper_function(6))



def main():
    number_generator()


if __name__ == "__main__":
    main()


