from unittest import TestCase
from dungeonsanddragons import combat_round
import random
import io
from unittest.mock import patch


class TestCombat_round(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('dungeonsanddragons.roll_die', side_effect=[2, 3, 6, 3, 7, 2])
    def test_combat_round_miss(self, mock_roll_die, mock_stdout):
        opponent_1 = {'Name': 'Te', 'Class': 'wizard', 'HP': 3, 'Strength': 10, 'Dexterity': 7,
                      'Constitution': 4, 'Intelligence': 4, 'Wisdom': 4, 'Charisma': 14, 'XP': 0, 'Inventory': ['Axe']}
        opponent_2 = {'Name': 'Ni', 'Class': 'monk', 'HP': 5, 'Strength': 6, 'Dexterity': 9, 'Constitution': 6,
                      'Intelligence': 16, 'Wisdom': 14, 'Charisma': 15, 'XP': 0, 'Inventory': ['Spear']}
        expected = ('Player 1 has rolled:  2 \n'
                    'Player 2 has rolled:  3 \n'
                    'Player 2 STRIKES first! \n'
                    ' --------------------\n'
                    'Ni MISSED the attack ,  Te DODGED\n'
                    ' Ni ATTACK unsuccessful!\n'
                    'Te MISSED the attack ,  Ni DODGED\n'
                    ' Te ATTACK unsuccessful!\n')
        combat_round(opponent_1, opponent_2)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('dungeonsanddragons.roll_die', side_effect=[2, 3, 10, 3, 7, 2])
    def test_combat_round_miss(self, mock_roll_die, mock_stdout):
        opponent_1 = {'Name': 'Te', 'Class': 'wizard', 'HP': 3, 'Strength': 10, 'Dexterity': 7,
                      'Constitution': 4, 'Intelligence': 4, 'Wisdom': 4, 'Charisma': 14, 'XP': 0,
                      'Inventory': ['Axe']}
        opponent_2 = {'Name': 'Ni', 'Class': 'monk', 'HP': 5, 'Strength': 6, 'Dexterity': 9, 'Constitution': 6,
                      'Intelligence': 16, 'Wisdom': 14, 'Charisma': 15, 'XP': 0, 'Inventory': ['Spear']}
        expected = ('Player 1 has rolled:  2 \n'
                    'Player 2 has rolled:  3 \n'
                    'Player 2 STRIKES first! \n'
                    ' --------------------\n'
                    'Ni STRUCK Te ,  Ni DEALT: 3 DAMAGE,  Te current HP is:  0 , ATTACK successful!\n'
                    ' ----------------------------------------------------------------------------------------------------\n'
                    'Te is dead! Ni is the winner!\n')
        combat_round(opponent_1, opponent_2)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('dungeonsanddragons.roll_die', side_effect=[2, 3, 10, 3, 7, 2])
    def test_combat_round_miss(self, mock_roll_die, mock_stdout):
        opponent_1 = {'Name': 'Te', 'Class': 'wizard', 'HP': 12, 'Strength': 10, 'Dexterity': 7,
                      'Constitution': 4, 'Intelligence': 4, 'Wisdom': 4, 'Charisma': 14, 'XP': 0,
                      'Inventory': ['Axe']}
        opponent_2 = {'Name': 'Ni', 'Class': 'monk', 'HP': 5, 'Strength': 6, 'Dexterity': 9, 'Constitution': 6,
                      'Intelligence': 16, 'Wisdom': 14, 'Charisma': 15, 'XP': 0, 'Inventory': ['Spear']}
        expected = ('Player 1 has rolled:  2 \n'
                    'Player 2 has rolled:  3 \n'
                    'Player 2 STRIKES first! \n'
                    ' --------------------\n'
                    'Ni STRUCK Te ,  Ni DEALT: 3 DAMAGE,  Te current HP is:  9 , ATTACK successful!\n'
                    ' ----------------------------------------------------------------------------------------------------\n'
                    'Te MISSED the attack ,  Ni DODGED\n'
                    ' Te ATTACK unsuccessful!\n')
        combat_round(opponent_1, opponent_2)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('dungeonsanddragons.roll_die', side_effect=[2, 3, 10, 3, 7, 2])
    def test_combat_round_miss(self, mock_roll_die, mock_stdout):
        opponent_1 = {'Name': 'Te', 'Class': 'wizard', 'HP': 2, 'Strength': 10, 'Dexterity': 7,
                      'Constitution': 4, 'Intelligence': 4, 'Wisdom': 4, 'Charisma': 14, 'XP': 0,
                      'Inventory': ['Axe']}
        opponent_2 = {'Name': 'Ni', 'Class': 'monk', 'HP': 5, 'Strength': 6, 'Dexterity': 9, 'Constitution': 6,
                      'Intelligence': 16, 'Wisdom': 14, 'Charisma': 15, 'XP': 0, 'Inventory': ['Spear']}
        expected = ('Player 1 has rolled:  2 \n'
                    'Player 2 has rolled:  3 \n'
                    'Player 2 STRIKES first! \n'
                    ' --------------------\n'
                    'Ni STRUCK Te ,  Ni DEALT: 3 DAMAGE,  Te current HP is:  -1 , ATTACK successful!\n'
                    ' ----------------------------------------------------------------------------------------------------\n'
                    'Te is dead! Ni is the winner!\n')
        combat_round(opponent_1, opponent_2)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('dungeonsanddragons.roll_die', side_effect=[2, 3, 10, 3, 20, 2])
    def test_combat_round_miss(self, mock_roll_die, mock_stdout):
        opponent_1 = {'Name': 'Te', 'Class': 'barbarian', 'HP': 12, 'Strength': 10, 'Dexterity': 7,
                      'Constitution': 4, 'Intelligence': 4, 'Wisdom': 4, 'Charisma': 14, 'XP': 0,
                      'Inventory': ['Axe']}
        opponent_2 = {'Name': 'Ni', 'Class': 'barbarian', 'HP': 12, 'Strength': 6, 'Dexterity': 9, 'Constitution': 6,
                      'Intelligence': 16, 'Wisdom': 14, 'Charisma': 15, 'XP': 0, 'Inventory': ['Spear']}
        expected = ('Player 1 has rolled:  2 \n'
                    'Player 2 has rolled:  3 \n'
                    'Player 2 STRIKES first! \n'
                    ' --------------------\n'
                    'Ni STRUCK Te ,  Ni DEALT: 3 DAMAGE,  Te current HP is:  9 , ATTACK successful!\n'
                    ' ----------------------------------------------------------------------------------------------------\n'
                    'Te STRUCK Ni ,  Te DEALT: 2 DAMAGE ,  Ni current HP is:  10 ,  ATTACK successful!\n'
                    ' ----------------------------------------------------------------------------------------------------\n')
        combat_round(opponent_1, opponent_2)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('dungeonsanddragons.roll_die', side_effect=[5, 3, 1, 3, 4, 3])
    def test_combat_round_miss(self, mock_roll_die, mock_stdout):
        opponent_1 = {'Name': 'Te', 'Class': 'barbarian', 'HP': 12, 'Strength': 10, 'Dexterity': 1,
                      'Constitution': 4, 'Intelligence': 4, 'Wisdom': 4, 'Charisma': 14, 'XP': 0,
                      'Inventory': ['Axe']}
        opponent_2 = {'Name': 'Ni', 'Class': 'barbarian', 'HP': 12, 'Strength': 6, 'Dexterity': 9, 'Constitution': 6,
                      'Intelligence': 16, 'Wisdom': 14, 'Charisma': 15, 'XP': 0, 'Inventory': ['Spear']}
        expected = ('Player 1 has rolled:  5 \n'
                    'Player 2 has rolled:  3 \n'
                    'Player 1 STRIKES first! \n'
                    ' --------------------\n'
                    'Te MISSED the attack ,  Ni DODGED\n'
                    ' Te ATTACK unsuccessful!\n'
                    'Ni STRUCK Te ,  Ni DEALT: 4 DAMAGE ,  Te current HP is:  8 ,  ATTACK successful!\n'
                    ' ----------------------------------------------------------------------------------------------------\n')
        combat_round(opponent_1, opponent_2)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('dungeonsanddragons.roll_die', side_effect=[5, 3, 1, 3, 4, 3])
    def test_combat_round_miss(self, mock_roll_die, mock_stdout):
        opponent_1 = {'Name': 'Te', 'Class': 'barbarian', 'HP': 1, 'Strength': 10, 'Dexterity': 1,
                      'Constitution': 4, 'Intelligence': 4, 'Wisdom': 4, 'Charisma': 14, 'XP': 0,
                      'Inventory': ['Axe']}
        opponent_2 = {'Name': 'Ni', 'Class': 'barbarian', 'HP': 12, 'Strength': 6, 'Dexterity': 9, 'Constitution': 6,
                      'Intelligence': 16, 'Wisdom': 14, 'Charisma': 15, 'XP': 0, 'Inventory': ['Spear']}
        expected = ('Player 1 has rolled:  5 \n'
                    'Player 2 has rolled:  3 \n'
                    'Player 1 STRIKES first! \n'
                    ' --------------------\n'
                    'Te MISSED the attack ,  Ni DODGED\n'
                    ' Te ATTACK unsuccessful!\n'
                    'Ni STRUCK Te ,  Ni DEALT: 4 DAMAGE ,  Te current HP is:  -3 ,  ATTACK successful!\n'
                    ' ----------------------------------------------------------------------------------------------------\n'
                    'Te is dead! Ni is the winner!\n')
        combat_round(opponent_1, opponent_2)
        self.assertEqual(mock_stdout.getvalue(), expected)
