from unittest import TestCase
from sud import combat_to_death
from unittest.mock import patch
import character
import random


class TestCombatToDeath(TestCase):

    @patch('random.randint', return_value=1)
    def test_combat_to_death_defeat(self, mock_random):
        # When character dies to monster.
        random.seed(1)
        combat_to_death()
        self.assertTrue(character.get_hp() == -2)

    @patch('random.randint', return_value=1)
    def test_combat_to_death_victory(self, mock_random):
        # When character dies to monster.
        random.seed(3)
        combat_to_death()
        self.assertTrue(character.get_hp() == 5)
