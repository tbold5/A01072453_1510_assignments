from unittest import TestCase
from q10 import database_shared_headings


class TestDatabase_shared_headings(TestCase):
    def test_database_shared_headings_type(self):
        mock_dict = {'student1': {'name': 'Trae'}, 'student2': {'hobby': 'swimming'}}
        self.assertEqual(set, type(database_shared_headings(mock_dict)))

    def test_database_shared_headings_length(self):
        mock_dict = {'student1': {'name': 'Trae'}, 'student2': {'hobby': 'swimming'}}
        self.assertEqual(0, len(database_shared_headings(mock_dict)))

    def test_database_shared_headings_intersection(self):
        mock_dict = {'student1': {'name': 'Trae'}, 'student2': {'name': 'Bold', 'hobby': 'swimming'}}
        expected = {'name'}
        actual = database_shared_headings(mock_dict)
        self.assertEqual(expected, actual)

    def test_database_shared_headings_empty(self):
        self.assertEqual(set(), database_shared_headings({}))
