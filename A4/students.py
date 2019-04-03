class Student:

    def __init__(self, first_name: str, last_name: str,
                 student_number: str,
                 student_status: bool,
                 student_grades: list):
        """Create a new student.  A student must have a non-empty name that is
            not composed entirely of whitespace.  The name will be stored in title
            case.  The student number must be in the format A########.  Grades is
            an optional parameter.  If it is not included, this student will be
            created with a new empty list of grades.  If the parameter is included
            when the __init__ method is invoked, the content of the grades list
            will be copied to this student's internal grades list.  If any
            requirement is not met, a ValueError will be thrown and the student
            object will not be created."""

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
        """Return a string representation of this student that looks like:
            FirstName LastName A######## True 90 80 76 100 62 42
            Useful for the print function."""
        grades = ''
        for grade in self.__student_grades:
            grades += str(grade) + ' '

        return self.__first_name + ' ' + self.__last_name + ' ' + self.__student_number + \
            ' ' + str(self.__status) + ' ' + grades

    def set_grade(self, new_grade):
        self.__student_grades.append(new_grade)

    def get_student_first_name(self):
        """Return the first name."""
        return self.__first_name

    def get_student_last_name(self):
        """Return the last name."""
        return self.__last_name

    def get_student_number(self):
        """Return the student number."""
        return self.__student_number

    def get_grade(self):
        """Return the student grade."""
        return self.__student_grades

    def update_grade(self, grades: list):
        """Add the specified grades in the list to this student's list of grades."""
        self.__student_grades.extend(grades)

    def calculate_student_gpa(self, student_grade: list) -> float or None:
        """Calculate and return the student's gpa as a float."""
        if len(student_grade) == 0:
            return None
        else:
            average_gpa = sum(student_grade) / len(student_grade)
            return average_gpa


def main():
    test = Student('Trae', 'Bold', 'A01072453', True, ['100'])
    print(test)


if __name__ == '__main__':
    main()
