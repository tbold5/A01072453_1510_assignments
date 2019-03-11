from unittest import TestCase
from sud import create_map


class TestCreateMap(TestCase):

    def test_create_map_type(self):
        self.assertEqual(list, type(create_map()))

    def test_create_map_type2(self):
        self.assertEqual(list, type(create_map()[0]))

    def test_create_map_index_error(self):
        with self.assertRaises(IndexError):
            create_map()[9][9]

    def test_create_map_result(self):
        expected = [['😼', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']]

        actual = create_map()
        self.assertEqual(expected, actual)
