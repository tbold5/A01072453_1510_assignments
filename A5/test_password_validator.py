from unittest import TestCase
from q07 import password_validator
from unittest.mock import patch


class TestPasswordValidator(TestCase):
    @patch('builtins.input', return_value='hello')
    def test_password_validator_short_length(self, mock_input):
        self.assertFalse(password_validator())

    @patch('builtins.input', return_value='helloThere3')
    def test_password_validator_true(self, mock_input):
        self.assertTrue(password_validator())

    @patch('builtins.input', return_value='')
    def test_password_validator_empty(self, mock_input):
        self.assertFalse(password_validator())

    @patch('builtins.input', return_value='helloThereHowareyou')
    def test_password_validator_long_length(self, mock_input):
        self.assertFalse(password_validator())

    @patch('builtins.input', return_value='hellomynameistrae')
    def test_password_validator_all_lower(self, mock_input):
        self.assertFalse(password_validator())

    @patch('builtins.input', return_value='HELLOMYNAMEISTRAE')
    def test_password_validator_all_upper(self, mock_input):
        self.assertFalse(password_validator())
