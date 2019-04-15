from unittest import TestCase
from q04 import selection_sort


class TestSelectionSort(TestCase):
    def test_selection_sort_type(self):
        self.assertEqual(list, type(selection_sort([1, 2, 3])))

    def test_selection_sort_length(self):
        mock_list = [1, 2, 3]
        sorted_list = selection_sort(mock_list)
        self.assertTrue(len(mock_list) == len(sorted_list))

    def test_selection_sort_ascending(self):
        mock_list = selection_sort([6, 3, 2, 8, 1])
        for i in range(0, len(mock_list) - 1):
            self.assertTrue(mock_list[i] <= mock_list[i + 1])

    def test_selection_sort_is_copy(self):
        unsorted_list = [1, 4, 3, 7]
        selection_sort(unsorted_list)
        self.assertTrue(unsorted_list == [1, 4, 3, 7])

    def test_selection_sort_empty_list(self):
        with self.assertRaises(ValueError):
            selection_sort([])

