import random

def number_generator():
    """Number Generator

    A function that generates random 6 digit lottery number.
    PRECONDITION: int, random numbers between 1-49.
    RETURN: random unique integers, in list from lowest to highest order.
    """

    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
               11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
               21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
               31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
               41, 42, 43, 44, 45, 46, 47, 48, 49]
    random_list = random.sample(my_list, 6)
    random_list.sort()
    return random_list



def main():
     print(number_generator())



if __name__ == "__main__":
    main()


