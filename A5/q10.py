"""COMP1510 Assignment 5: Back to basics"""

# Trae Bold
# A01072453
# JAN 11, 2019

import doctest


def database_shared_headings(db_dictionary: dict) -> set:
    """Return set of keys.

    A that takes dictionary of dictonaries and returns set of keys used in all of inner dictionaries.
    PRECONDITION: dictionary keys has to be strings and its values must be a dictionary.
    PARAM: db_dictionary, a dictionary.
    RETURN: a set that contains all the keys used in inner dictionaries.
    >>> database_shared_headings({'student1': {'name': 'Trae', 'student_number': 'A01072453'}, 'student2': {'name': 'Bob'}})
    {'name'}
    >>> database_shared_headings({'student1': {'name': 'Trae'}, 'student2': {'hobby': 'swimming'}})
    set()
    """
    # Create empty set for unique values.
    all_info_set = set()

    # Populate the set with every information.
    for child_dictionary in db_dictionary.values():
        for info in child_dictionary.keys():
            if info not in all_info_set:
                all_info_set.add(info)

    # Loop through the dictionary and update the set through intersection to values that exist on both sides.
    for child_dictionary in db_dictionary.values():
        all_info_set = all_info_set.intersection(child_dictionary.keys())
    return all_info_set


def main():
    print(database_shared_headings({
        'jgoodall': {'surname': 'Goodall',
                        'name': 'Jane',
                        'born': 1934},
        'rfranklin': {'surname': 'Franklin',
                        'name': 'Rosalind',
                        'born': 1920,
                        'died': 1957}}))


if __name__ == '__main__':
    main()
