from unittest import TestCase
from sud import monster_encounter
from unittest.mock import patch
import random
import character


class TestMonsterEncounter(TestCase):

    @patch('builtins.input', return_value='2')
    @patch('sud.is_encounter_monster', return_value=True)
    def test_monster_encounter_flee(self, mock_input, mock_encounter_value):
        # Character successfully flees from monster.
        random.seed(1)
        monster_encounter()
        expected = 10
        actual = character.get_hp()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='1')
    @patch('sud.is_encounter_monster', return_value=True)
    def test_monster_encounter_combat_death(self, mock_input, mock_encounter_value):
        # Case when character duels monster and dies.
        random.seed(1)
        monster_encounter()
        expected = -2
        actual = character.get_hp()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='1')
    @patch('sud.is_encounter_monster', return_value=True)
    def test_monster_encounter_combat_victory(self, mock_input, mock_encounter_value):
        # Case when character duels monster and wins.
        random.seed(3)
        monster_encounter()
        expected = 5
        actual = character.get_hp()
        self.assertEqual(expected, actual)
