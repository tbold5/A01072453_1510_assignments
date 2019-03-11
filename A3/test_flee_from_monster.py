from unittest import TestCase
from sud import flee_from_monster
from unittest.mock import patch
import character
import random


class TestFleeFromMonster(TestCase):

    @patch('random.randint', return_value=1)
    def test_flee_from_monster_damage(self, mock_random):
        # When monster successfully attack while user tries to escape.
        random.seed(2)
        flee_from_monster()
        self.assertTrue(character.get_hp() == 9)

    @patch('random.randint', return_value=1)
    def test_flee_from_monster_no_damage(self, mock_random):
        # When user successfully escapes from the monster.
        random.seed(0)
        flee_from_monster()
        self.assertTrue(character.get_hp() == 10)
