from unittest import TestCase
from sud import is_max_health
from unittest.mock import patch


class TestIsMaxHealth(TestCase):

    @patch('character.get_hp', return_value=10)
    def test_is_max_health_true(self, mock_get_hp):
        expected = True
        actual = is_max_health()
        is_max_health()
        self.assertEqual(expected, actual)

    # Return False when character HP is less than 10
    @patch('character.get_hp', return_value=0)
    def test_is_max_health_false(self, mock_get_hp):
        expected = False
        actual = is_max_health()
        is_max_health()
        self.assertEqual(expected, actual)

    @patch('character.get_hp', return_value=10)
    def test_is_max_health_type(self, mock_get_hp):
        is_max_health()
        self.assertEqual(bool, type(is_max_health()))
