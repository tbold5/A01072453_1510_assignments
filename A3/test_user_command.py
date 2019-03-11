from unittest import TestCase
from sud import user_command
from unittest.mock import patch


class TestUserCommand(TestCase):

    @patch('builtins.input', return_value='1')
    def test_user_command_type(self, mock_user_command):
        self.assertEqual(str, type(user_command()))

    @patch('builtins.input', return_value='5')
    def test_user_command_valid_input(self, mock_user_command):
        self.assertEqual('5', user_command())

    @patch('builtins.input', return_value='7')
    def test_user_command_valid_input(self, mock_user_command):
        expected = None
        actual = user_command()
        self.assertEqual(expected, actual)
