from unittest import TestCase
from crud import get_student_number_list
from unittest.mock import patch, mock_open


class TestGetStudentNumberList(TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='Trae Bold A01072453 True 100')
    def test_get_student_number_list(self, mock_file):
        expected = ['A01072453']
        actual = get_student_number_list()
        self.assertEqual(expected, actual)

    @patch('builtins.open', new_callable=mock_open, read_data='')
    def test_get_student_number_empty_list(self, mock_file):
        expected = []
        actual = get_student_number_list()
        self.assertEqual(expected, actual)

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_get_student_number_file_not_found(self, mock_open):
        with self.assertRaises(FileNotFoundError):
            get_student_number_list()
