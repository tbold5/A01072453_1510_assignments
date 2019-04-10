"""COMP1510 Assignment 5: Back to basics"""

# Trae Bold
# A01072453
# JAN 11, 2019


def backup(file_name: str):
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
