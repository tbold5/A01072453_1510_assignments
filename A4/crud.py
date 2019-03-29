from students import Student


def add_student():
    first_name = input('Student First Name?: ').strip().title()
    last_name = input('Student Last Name?: ').strip().title()
    student_number = input('Student Number?: ').strip().upper()
    student_status = is_in_good_standing(input('Student Status? 1) Good standing / 2) Bad standing'))

    mock_student = Student(first_name, last_name, student_number, student_status)
    student_info = str(mock_student)
    file_name = 'students.txt'
    with open(file_name, 'a') as file_object:
        file_object.write(student_info + '\n')


def is_in_good_standing(user_choice):
    if user_choice == '1':
        return True
    elif user_choice == '2':
        return False
    else:
        pass


def main():
    user_choice = ''
    while user_choice != '5':
        user_choice = input(""" 
        1. Add student
        2. Delete student
        3. Calculate class average
        4. Print class list
        5. Quit
        """)
        if user_choice == '1':
            try:
                add_student()
            except ValueError as e:
                print(e)


if __name__ == '__main__':
    main()
