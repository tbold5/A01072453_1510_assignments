from unittest import TestCase
from crud import add_student
from unittest.mock import patch, mock_open
import io


class TestAddStudent(TestCase):

    @patch('builtins.open', new_callable=mock_open)
    @patch('builtins.input', side_effect=['Trae', 'Bold', 'A01072453', '1', '100', 'q'])
    def test_add_student(self, mock_input, mock_file):
        expected = 'Trae Bold A01072453 True 100 \n'
        actual = add_student()
        mock_file().write.assert_called_once_with(expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['Trae', 'Bold', 'A01072453', '1', '100', 'q'])
    @patch('crud.is_valid_student_number', return_value= False)
    def test_add_student_duplicate_student_number(self, mock_input, mock_valid_number, mock_stdout):
        expected = "\nStudent number already exist!\n\n"
        add_student()
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['', 'Bold', 'A01072453', '1', '100', 'q'])
    @patch('crud.is_valid_student_number', return_value=False)
    def test_add_student_invalid_first_name(self, mock_input, mock_valid_number, mock_stdout):
        expected = "\nStudent number already exist!\n\n"
        with self.assertRaises(ValueError):
            add_student()

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['Trae', '', 'A01072453', '1', '100', 'q'])
    @patch('crud.is_valid_student_number', return_value=False)
    def test_add_student_invalid_last_name(self, mock_input, mock_valid_number, mock_stdout):
        with self.assertRaises(ValueError):
            add_student()

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['Trae', 'Bold', '01072453', '1', '100', 'q'])
    @patch('crud.is_valid_student_number', return_value=False)
    def test_add_student_invalid_student_number(self, mock_input, mock_valid_number, mock_stdout):
        with self.assertRaises(ValueError):
            add_student()
