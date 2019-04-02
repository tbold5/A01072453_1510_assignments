class Student:
    def __init__(self, first_name: str, last_name: str, student_number: str,
                 student_status: bool, student_grades: list):

        # Checks conditions for first_name and last_name.
        if len(first_name) == 0 or len(last_name) == 0:
            raise ValueError('\nName must contain letters!\n')
        else:
            self.__first_name = first_name
            self.__last_name = last_name

        # Checks conditions for student_number.
        if student_number[0] != "A" or not student_number[1:9].isdigit() or len(student_number) != 9:
            raise ValueError('\nStudent number should start with "A" followed by 8 digits numbers\n')
        else:
            self.__student_number = student_number

        self.__status = student_status

        # Check conditions for student grades.
        if student_grades == list():
            self.__student_grades = student_grades

        for grade in student_grades:
            if int(grade) < 0 or int(grade) > 100:
                raise ValueError('\nGrades must be numbers between 0 - 100\n')
            else:
                self.__student_grades = student_grades

    def __str__(self):
        grades = ''
        for grade in self.__student_grades:
            grades += str(grade) + ' '

        return self.__first_name + ' ' + self.__last_name + ' ' + self.__student_number + \
               ' ' + str(self.__status) + ' ' + grades

    def set_grade(self, new_grade):
        self.__student_grades.append(new_grade)

    def get_grade(self):
        return self.__student_grades

    def get_student_last_name(self):
        return self.__last_name

    def get_student_number(self):
        return self.__student_number

    def update_grade(self, grades: list):
        self.__student_grades.extend(grades)


def main():
    test = Student('Trae', 'Bold', 'A01072453', True, ['100'])
    print(test)


if __name__ == '__main__':
    main()
