from students import Student


def add_student():
    first_name = input('Student First Name?: ').strip().title()
    last_name = input('Student Last Name?: ').strip().title()
    student_number = input('Student Number?: ').strip().upper()
    student_status = is_in_good_standing(input('Student Status? 1) Good standing / 2) Bad standing'))
    student_grades = add_grade()
    mock_student = Student(first_name, last_name, student_number, student_status, student_grades)
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


def add_grade():
    student_grades = []
    while True:
        user_choice = input('Please provide Student Grade(s) (0 - 100) / press "q" when finished: ').lower()
        if user_choice.isdigit():
            student_grades.append(int(user_choice))
        elif user_choice != 'q':
            print('Grade must be integer between 0 - 100')
        elif user_choice == 'q':
            break
    return student_grades


def delete_student():
    student_number = input('To delete student provide Student Number: ').upper()
    with open('students.txt', 'r+') as file_object:
        for student in file_read():
            if student_number == student.get_student_number():
                file_object.seek(0)
                lines = file_object.readlines()
                file_object.seek(0)
                for line in lines:
                    if student_number not in line:
                        file_object.write(line)
                file_object.truncate()
                return True
            else:
                print('\nStudent number does not exist!\n')
                return False


def file_read():
    student_list = []
    with open('students.txt', 'r') as file_object:
        for line in file_object.readlines():
            info = line.split()

            if info[3] == 'True':
                info[3] = 1
            else:
                info[3] = 0

            student_grades = []
            for grade in info[4:]:
                student_grades.append(int(grade))

            # Assign each student to a student object.
            student_object = Student(info[0], info[1], info[2], bool(info[3]), student_grades)
            student_list.append(student_object)
        return student_list


def calculate_student_gpa(student_grade: list):
    average_gpa = sum(student_grade) / len(student_grade)
    return average_gpa


def calculate_class_gpa():
    student_gpa = [calculate_student_gpa(element.get_grade()) for element in file_read()]
    class_avg = sum(student_gpa) / len(student_gpa)
    return class_avg


def print_class_list():
    class_list = []
    for student in file_read():
        class_list.append([student.get_student_last_name(), student])
    sorted_last_name = sorted(class_list)
    for student in sorted_last_name:
        print(student[1])


def add_new_grade():
    student_number = input('Please provide Student Number: ').upper()
    class_list = file_read()
    updated_grade = False
    for student in class_list:
        if student_number == student.get_student_number():
            student.update_grade(add_grade())
            updated_grade = True
    if updated_grade:
        print('\nStudent graded added successfully!')
        with open('students.txt', 'w') as file_object:
            for student_obj in class_list:
                file_object.write(str(student_obj) + '\n')
    else:
        print('\nStudent number not found!')


def main():
    user_choice = ''
    while user_choice != '5':
        user_choice = input("""
        1. Add student
        2. Delete student
        3. Calculate class average
        4. Print class list by last name
        5. Quit
        6. Add grade
        """)
        # Add student method.
        if user_choice == '1':
            try:
                add_student()
            except ValueError as e:
                print(e)

        # Delete student method.
        elif user_choice == '2':
            if delete_student():
                print('\nStudent deleted successfully\n')
            else:
                print('Delete student unsuccessful\n')

        # Calculate class average method.
        elif user_choice == '3':
            try:
                print('Class average: ', round(calculate_class_gpa(), 2))
            except ZeroDivisionError:
                print('\nClass list is empty, can not divide by 0.')

        # Print class info method.
        elif user_choice == '4':
            print_class_list()

        # Add grade method
        elif user_choice == '6':
            add_new_grade()

        else:
            print('\n***Please choose a valid option***\n')


if __name__ == '__main__':
    main()
