from unittest import TestCase
from crud import delete_student
from unittest.mock import patch, mock_open


class TestDeleteStudent(TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='Trae Bold A01072453 True 100')
    @patch('builtins.input', side_effect=['A01072453'])
    def test_delete_student_true(self, mock_file, mock_input):
        expected = True
        actual = delete_student()
        self.assertEqual(expected, actual)

    @patch('builtins.open', new_callable=mock_open, read_data='Trae Bold A01072453 True 100')
    @patch('builtins.input', side_effect=['A99999999'])
    def test_delete_student_false(self, mock_file, mock_input):
        expected = False
        actual = delete_student()
        self.assertEqual(expected, actual)

    @patch('builtins.open', new_callable=mock_open, read_data='Trae Bold A01072453 True 100')
    @patch('builtins.input', side_effect=['A01072453'])
    def test_delete_student_type(self, mock_file, mock_input):
        expected = bool
        actual = type(delete_student())
        self.assertEqual(expected, actual)
