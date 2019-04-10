"""COMP1510 Assignment 5: Back to basics"""

# Trae Bold
# A01072453
# JAN 11, 2019

import re


def password_validator() -> bool:
    while True:
        user_input = input('Provide password: ')

        length_regex = re.compile(r'.{8,}')
        length_match = length_regex.search(user_input)

        upper_case_regex = re.compile(r'[A-Z]')
        upper_case_match = upper_case_regex.search(user_input)

        lower_case_regex = re.compile(r'[a-z]')
        lower_case_match = lower_case_regex.search(user_input)

        digit_regex = re.compile(r'\d')
        digit_match = digit_regex.search(user_input)

        if length_match and upper_case_match and lower_case_match and digit_match:
            print('Password updated successfully!')
            return True
        else:
            print('Password too weak!')
            return False


def main():
    password_validator()


if __name__ == '__main__':
    main()
