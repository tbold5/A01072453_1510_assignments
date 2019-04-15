"""COMP1510 Assignment 5: Back to basics"""

# Trae Bold
# A01072453
# JAN 11, 2019

import doctest


def backup(file_name: str):
    """Backup a file.

    A function that accepts file_name as string
    and creates new file in the same directory with some content but with .bak extension.
    PARAM: file_name, a string.
    POSTCONDTION: prints helpful message if the file backed up successfully or not.
    >>> backup('students.txt')
    Generated students.bak file successfully!
    """
    formatted_name = file_name.replace('.txt', '.bak')
    try:
        with open(file_name, 'r') as file_object:
            lines = file_object.readlines()
        with open(formatted_name, 'w') as object_file:
            for line in lines:
                object_file.write(line)
    except FileNotFoundError:
        print('File does not exist!')
    else:
        print('Generated ' + formatted_name + ' file successfully!')


def main():
    backup('students.txt')


if __name__ == '__main__':
    main()
