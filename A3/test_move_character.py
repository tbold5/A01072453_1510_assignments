from unittest import TestCase
from sud import move_character
from unittest.mock import patch
import io
import character


class TestMoveCharacter(TestCase):

    @patch('sud.user_command', return_value='3')
    @patch('sud.is_max_health', return_value=True)
    @patch('sud.is_valid_move', return_value=True)
    def test_move_character_move_south(self, mock_validMove, mock_maxHealth, mock_input):
        # Increases character.get_position()[0] by +1
        expected = character.get_position()
        result = [1, 0]
        move_character(user_choice='2', max_hp=10)
        self.assertEqual(expected, result)

    @patch('sud.user_command', return_value='1')
    @patch('sud.is_max_health', return_value=True)
    @patch('sud.is_valid_move', return_value=True)
    def test_move_character_move_north(self, mock_validMove, mock_maxHealth, mock_input):
        # Decreases character.get_position()[0] by -1.
        expected = character.get_position()
        move_character(user_choice='1', max_hp=10)
        result = [-1, 0]
        self.assertEqual(expected, result)

    @patch('sud.user_command', return_value='1')
    @patch('sud.is_max_health', return_value=True)
    @patch('sud.is_valid_move', return_value=True)
    def test_move_character_move_east(self, mock_validMove, mock_maxHealth, mock_input):
        # Increases character.get_position()[1] by +1.
        expected = character.get_position()
        move_character(user_choice='3', max_hp=10)
        result = [0, 1]
        self.assertEqual(expected, result)

    @patch('sud.user_command', return_value='1')
    @patch('sud.is_max_health', return_value=True)
    @patch('sud.is_valid_move', return_value=True)
    def test_move_character_move_west(self, mock_validMove, mock_maxHealth, mock_input):
        # Decreases character.get_position()[1] by -1.
        expected = character.get_position()
        move_character(user_choice='4', max_hp=10)
        result = [0, -1]
        self.assertEqual(expected, result)

    @patch('builtins.input', return_value='2')
    @patch('sud.user_command', return_value='4')
    @patch('sud.is_max_health', return_value=False)
    @patch('sud.is_valid_move', return_value=True)
    @patch('character.get_hp', return_value=9)
    def test_move_character_move_check_out_of_bound_move(self, mock_input, mock_get_hp,
                                                  mock_validMove, mock_maxHealth, mock_user_command):
        # Set character HP to 9 and initialize out of bound move,
        # to check if HP stays the same as character tries invalid move.
        move_character(user_choice='1', max_hp=False)
        self.assertTrue(character.get_hp() == 9)

    @patch('builtins.input', return_value='2')
    @patch('sud.user_command', return_value='4')
    @patch('sud.is_max_health', return_value=True)
    @patch('sud.is_valid_move', return_value=True)
    def test_move_character_move_check_not_increaseHP(self, mock_input, mock_get_hp, mock_validMove, mock_maxHealth,):
        # Initialize valid move when character has max HP to check if HP exceeds over 10.
        move_character(user_choice='1', max_hp=True)
        self.assertTrue(character.get_hp() == 10)
