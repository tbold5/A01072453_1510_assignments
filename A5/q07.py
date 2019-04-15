"""COMP1510 Assignment 5: Back to basics"""

# Trae Bold
# A01072453
# JAN 11, 2019

import re


def password_validator() -> bool:
    user_input = input('Provide password: ')

    length_match = re.compile(r'.{8,}').search(user_input)

    upper_case_match = re.compile(r'[A-Z]').search(user_input)

    lower_case_match = re.compile(r'[a-z]').search(user_input)

    digit_match = re.compile(r'\d').search(user_input)

    if length_match and upper_case_match and lower_case_match and digit_match:
        print('Password updated successfully!')
        return True
    else:
        print('Password too weak!')
        return False


def main():
    while True:
        password_validator()


if __name__ == '__main__':
    main()
