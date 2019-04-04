from unittest import TestCase
from crud import add_grade
from unittest.mock import patch
import io


class TestAddGrade(TestCase):
    @patch('builtins.input', side_effect=['100', '99', 'q'])
    def test_add_grade(self, mock_input):
        expected = [100, 99]
        actual = add_grade()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['q'])
    def test_add_grade_empty_list(self, mock_input):
        expected = []
        actual = add_grade()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['100', '99', 'q'])
    def test_add_grade_type(self, mock_input):
        expected = list
        actual = type(add_grade())
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['z', 'q'])
    def test_add_grade_invalid_input(self, mock_input, mock_stdout):
        expected = 'Grade must be integer between 0 - 100\n'
        add_grade()
        self.assertEqual(expected, mock_stdout.getvalue())
