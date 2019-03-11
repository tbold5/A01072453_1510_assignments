from unittest import TestCase
from sud import is_encounter_monster
import random


class TestIsEncounterMonster(TestCase):

    def test_is_encounter_monster_False(self):
        random.seed(1)
        expected = False
        actual = is_encounter_monster()
        self.assertEqual(expected, actual)

    def test_is_encounter_monster_True(self):
        random.seed(2)
        expected = True
        actual = is_encounter_monster()
        self.assertEqual(expected, actual)

    def test_is_encounter_monster_type(self):
        self.assertTrue(type(is_encounter_monster()) == bool)
