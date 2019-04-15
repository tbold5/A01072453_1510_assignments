"""COMP1510 Assignment 5: Back to basics"""

# Trae Bold
# A01072453
# JAN 11, 2019

from copy import copy
import doctest


def selection_sort(unsorted_list: list) -> list:
    """Sort a list.

    A function that takes non-empty list and returns a sorted copy.
    PRECONDITION: unsorted_list has to be non-empty list.
    PARAM: unsorted_list, a list.
    RETURN: sorted copy list.
    >>> selection_sort([12, 5, 2, 6])
    [2, 5, 6, 12]
    """
    if len(unsorted_list) == 0:
        raise ValueError('List must contain sortable items!')
    else:
        copy_list = copy(unsorted_list)
        for index in range(len(copy_list)):
            # Store current small number as variable and assign it to temporary variable.
            current_small = copy_list[index]
            temp = current_small
            for value in range(index, len(copy_list)):
                if copy_list[value] < current_small:
                    current_small = copy_list[value]
            # Store index of smallest number and index of swapping number.
            swap_index = copy_list.index(current_small)
            copy_list[index] = current_small
            copy_list[swap_index] = temp
    return copy_list


def main():
    try:
        print(selection_sort([]))
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
