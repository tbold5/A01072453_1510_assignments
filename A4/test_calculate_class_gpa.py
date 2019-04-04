from unittest import TestCase
from crud import calculate_class_gpa
from unittest.mock import patch, mock_open


class TestCalculateClassGpa(TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='Trae Bold A01072453 True 100 99 88')
    def test_calculate_class_gpa(self, mock_open):
        expected = 95.67
        actual = round(calculate_class_gpa(), 2)
        self.assertEqual(expected, actual)

    @patch('builtins.open', new_callable=mock_open, read_data='Trae Bold A01072453 True 100 99 88')
    def test_calculate_class_gpa_type(self, mock_open):
        expected = float
        actual = type(calculate_class_gpa())
        self.assertEqual(expected, actual)

    @patch('builtins.open', new_callable=mock_open, read_data='Trae Bold A01072453 True')
    def test_calculate_class_gpa_is_none(self, mock_open):
        expected = []
        with self.assertRaises(AttributeError):
            calculate_class_gpa()
