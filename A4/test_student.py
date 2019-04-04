from unittest import TestCase
from students import Student


class TestStudent(TestCase):

    def setUp(self):
        self.test_student = Student('Trae', 'Bold', 'A01072453', True, [100, 99, 88, 77])

    def test_set_grade_positive(self):
        expected = [100, 99, 88, 77, 66]
        self.test_student.set_grade(66)
        self.assertEqual(expected, self.test_student.get_grade())

    def test_set_grade_negative(self):
        expected = [100, 99, 88, 77]
        self.test_student.set_grade(-66)
        self.assertEqual(expected, self.test_student.get_grade())

    def test_set_grade_exceeding_number(self):
        expected = [100, 99, 88, 77]
        self.test_student.set_grade(101)
        self.assertEqual(expected, self.test_student.get_grade())

    def test_set_grade_type(self):
        expected = list
        self.test_student.set_grade(-66)
        self.assertEqual(expected, type(self.test_student.get_grade()))

    def test_get_student_first_name_correct(self):
        expected = "Trae"
        self.test_student.get_student_first_name()
        self.assertEqual(expected, self.test_student.get_student_first_name())

    def test_get_student_first_name_type(self):
        expected = str
        actual = type(self.test_student.get_student_first_name())
        self.assertEqual(expected, actual)

    def test_get_student_last_name_correct(self):
        expected = "Bold"
        self.test_student.get_student_last_name()
        self.assertEqual(expected, self.test_student.get_student_last_name())

    def test_get_student_last_name_type(self):
        expected = str
        actual = type(self.test_student.get_student_last_name())
        self.assertEqual(expected, actual)

    def test_get_student_number(self):
        expected = 'A01072453'
        actual = self.test_student.get_student_number()
        self.assertEqual(expected, actual)

    def test_get_student_number_type(self):
        expected = str
        actual = type(self.test_student.get_student_number())
        self.assertEqual(expected, actual)

    def test_get_grade(self):
        expected = [100, 99, 88, 77]
        actual = self.test_student.get_grade()
        self.assertEqual(expected, actual)

    def test_get_grade_type(self):
        expected = list
        actual = type(self.test_student.get_grade())
        self.assertEqual(expected, actual)

    def test_update_grade(self):
        expected = [100, 99, 88, 77, 66, 55, 44]
        self.test_student.update_grade([66, 55, 44])
        self.assertEqual(expected, self.test_student.get_grade())

    def test_update_grade_type(self):
        expected = list
        self.test_student.update_grade([66, 55, 44])
        self.assertEqual(expected, type(self.test_student.get_grade()))

    def test_calculate_student_gpa(self):
        expected = 91.0
        actual = self.test_student.calculate_student_gpa([100, 99, 88, 77])
        self.assertEqual(expected, actual)

    def test_calculate_student_gpa_type(self):
        expected = float
        actual = type(self.test_student.calculate_student_gpa([100, 99, 88, 77]))
        self.assertEqual(expected, actual)

    def test_student_status(self):
        expected = True
        actual = self.test_student.get_student_status()
        self.assertEqual(expected, actual)

    def test_student_status_type(self):
        expected = bool
        actual = type(self.test_student.get_student_status())
        self.assertEqual(expected, actual)

