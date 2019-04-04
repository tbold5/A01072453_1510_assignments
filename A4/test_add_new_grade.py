from unittest import TestCase
from crud import add_new_grade
from unittest.mock import patch, mock_open
import io


class TestAddNewGrade(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['A01072453', '100', 'q'])
    @patch('builtins.open', new_callable=mock_open, read_data='Trae Bold A01072453 True 100\n Maria Kim A00112233 False 88')
    def test_add_new_grade_found(self, mock_input, mock_open, mock_stdout):
        expected = '\nStudent graded added successfully!\n'
        add_new_grade()
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['A99999999', '100', 'q'])
    @patch('builtins.open', new_callable=mock_open,
           read_data='Trae Bold A01072453 True 100\n Maria Kim A00112233 False 88')
    def test_add_new_grade_not_found(self, mock_input, mock_open, mock_stdout):
        expected = '\nStudent number not found!\n'
        add_new_grade()
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['A01072453', '999', 'q'])
    @patch('builtins.open', new_callable=mock_open,
           read_data='Trae Bold A01072453 True 100\n Maria Kim A00112233 False 88')
    def test_add_new_grade_value_error(self, mock_input, mock_open):
        with self.assertRaises(ValueError):
            add_new_grade()
