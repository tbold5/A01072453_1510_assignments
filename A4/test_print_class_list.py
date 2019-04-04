from unittest import TestCase
from crud import print_class_list
from unittest.mock import patch, mock_open
import io


class TestPrintClassList(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.open', new_callable=mock_open, read_data='Trae Bold A01072453 True 100\n Maria Kim A00112233 False 88')
    def test_print_class_list(self, mock_open, mock_stdout):
        expected = """Trae Bold A01072453 True 100 
Maria Kim A00112233 False 88 
"""
        print_class_list()
        self.assertEqual(expected, mock_stdout.getvalue())
