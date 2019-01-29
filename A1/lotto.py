import random

def number_generator():
    """Number Generator

        A function that generates random 6 digit lottery number
        PRE: int, random numbers between 1-49
        RETURN: in list from highest to lowest order
    """
    return helper_function(6)


def helper_function(x):
    if x == 0:
        return []
    else:
        #add random integers from 1 - 49 to the list
        list = helper_function(x - 1)
        r = random.randint(1,50)
        list.append(r)
        #if r not in list: list.append(r)
        #random.shuffle(list)
        my_list = list
        my_list.sort()
        return my_list


def main():
    print(number_generator())


if __name__ == "__main__":
    main()


