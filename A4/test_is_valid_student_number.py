from unittest import TestCase
from crud import is_valid_student_number
from unittest.mock import patch


class TestIsValidStudentNumber(TestCase):

    @patch('crud.get_student_number_list', side_effect=['A01072453'])
    def test_is_valid_student_number_false(self, mock_list):
        self.assertEqual(False, is_valid_student_number('A01072453'))

    @patch('crud.get_student_number_list', side_effect=['A0000000'])
    def test_is_valid_student_number_true(self, mock_list):
        self.assertEqual(True, is_valid_student_number('A01072453'))

    @patch('crud.get_student_number_list', side_effect=['A0000000'])
    def test_is_valid_student_number_type(self, mock_list):
        self.assertEqual(bool, type(is_valid_student_number('A01072453')))
