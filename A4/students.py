class Student:
    def __init__(self, first_name: str, last_name: str, student_number: str, status: bool):
        if len(first_name) == 0 or len(last_name) == 0:
            raise ValueError('Name must contain letters!')
        else:
            self.__first_name = first_name
            self.__last_name = last_name

        if student_number[0] != "A" or not student_number[1:9].isdigit() or len(student_number) != 9:
            raise ValueError('Student number should start with A followed by 8 digits numbers')
        else:
            self.__student_number = student_number

        self.__status = status
        self.__final_grades = []

    def __str__(self):
        return self.__first_name + ' ' + self.__last_name + ' ' + self.__student_number + ' ' + str(self.__status)

    # def set_grade(self):


def main():
    test = Student('Trae', 'Bold', 'A01072453', True)
    print(test)


if __name__ == '__main__':
    main()
