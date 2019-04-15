from unittest import TestCase
from q03 import backup
from unittest.mock import patch, mock_open
import io


class TestBackup(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.open', new_callable=mock_open, read_data='Zen of Python')
    def test_backup_does_exist(self, mock_file, mock_stdout):
        expected = 'Generated zen.bak file successfully!\n'
        backup('zen.txt')
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_backup_does_not_exist(self, mock_stdout):
        expected = 'File does not exist!\n'
        backup('student.txt')
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('builtins.open', new_callable=mock_open, read_data='Zen of Python')
    def test_backup_check_content(self, mock_file):
        backup('zen.txt')
        with open('zen.text') as f_obj:
            content_txt = f_obj.read()
        with open('zen.bak') as f_obj:
            content_bak = f_obj.read()
        self.assertTrue(content_txt == content_bak)
