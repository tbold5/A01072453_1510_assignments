from unittest import TestCase
from crud import file_read
from unittest.mock import patch, mock_open


class TestFileRead(TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='Trae Bold A01072453 True 100')
    def test_file_read_first_name(self, mock_open):
        expected = 'Trae'
        for student in file_read():
            actual = student.get_student_first_name()
        self.assertEqual(expected, actual)

    @patch('builtins.open', new_callable=mock_open, read_data='Trae Bold A01072453 True 100')
    def test_file_read_last_name(self, mock_open):
        expected = 'Bold'
        for student in file_read():
            actual = student.get_student_last_name()
        self.assertEqual(expected, actual)

    @patch('builtins.open', new_callable=mock_open, read_data='Trae Bold A01072453 True 100')
    def test_file_read_student_number(self, mock_open):
        expected = 'A01072453'
        for student in file_read():
            actual = student.get_student_number()
        self.assertEqual(expected, actual)

    @patch('builtins.open', new_callable=mock_open, read_data='Trae Bold A01072453 True 100')
    def test_file_read_student_status(self, mock_open):
        expected = True
        for student in file_read():
            actual = student.get_student_status()
        self.assertEqual(expected, actual)

    @patch('builtins.open', new_callable=mock_open, read_data='Trae Bold A01072453 True 100')
    def test_file_read_student_grade(self, mock_open):
        expected = [100]
        for student in file_read():
            actual = student.get_grade()
        self.assertEqual(expected, actual)

    @patch('builtins.open', new_callable=mock_open, read_data='Trae Bold A01072453 True 100')
    def test_file_read_type_list(self, mock_open):
        expected = list
        actual = type(file_read())
        self.assertEqual(expected, actual)

