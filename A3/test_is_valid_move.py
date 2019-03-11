from unittest import TestCase
from sud import is_valid_move
from sud import user_command
import io
from unittest.mock import patch


class TestIsValidMove(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value=1)
    @patch('character.get_position', return_value=[4, 4])
    def test_is_valid_move_is_inbound(self, mock_user_choice, mock_user_position, mock_stdout):
        expected = True
        actual = is_valid_move(user_command())
        is_valid_move(user_command())
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='1')
    @patch('character.get_position', return_value=[0, 0])
    def test_is_valid_move_is_out_of_bound_north(self, mock_user_choice, mock_user_position, mock_stdout):

        # When user tries to move north while being in first column will return False.
        expected = False
        actual = is_valid_move(user_command())
        is_valid_move(user_command())
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='2')
    @patch('character.get_position', return_value=[7, 0])
    def test_is_valid_move_is_out_of_bound_south(self, mock_user_choice, mock_user_position, mock_stdout):
        # When user tries to move north while being in first column will return False.
        expected = False
        actual = is_valid_move(user_command())
        is_valid_move(user_command())
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='3')
    @patch('character.get_position', return_value=[7, 7])
    def test_is_valid_move_is_out_of_bound_east(self, mock_user_choice, mock_user_position, mock_stdout):
        # When user tries to move north while being in first column will return False.
        expected = False
        actual = is_valid_move(user_command())
        is_valid_move(user_command())
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='4')
    @patch('character.get_position', return_value=[7, 0])
    def test_is_valid_move_is_out_of_bound_south(self, mock_user_choice, mock_user_position, mock_stdout):
        # When user tries to move north while being in first column will return False.
        expected = False
        actual = is_valid_move(user_command())
        is_valid_move(user_command())
        self.assertEqual(expected, actual)
