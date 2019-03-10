"""COMP1510 Assignment # 3: Your First SUD!"""

# Trae Bold
# A01072453
# JAN 11, 2019


from random import randint

monster = {'Name': 'Chocolator', 'HP': 5, 'Damage:': 0}


def get_name():
    """Gets the name from the dictionary.

    RETURN: Name, key from the monster dictionary."""

    return monster['Name']


def get_hp():
    """Gets the HP from the dictionary.

    RETURN: HP, key from the monster dictionary."""

    return monster['HP']


def get_damage():
    """Gets the damage from the dictionary.

    RETURN: Damage, key from the monster dictionary."""

    return monster['Damage']


def get_monster():
    """Gets monster keys and values from the dictionary.

    RETURN: monster, dictionary containing monster key value pairs."""
    return monster


def decrease_hp():
    """Decrease HP by random numbers between 1 - 6.

    A function that modifies monster HP value numbers between 1 - 6 when called."""
    global monster
    monster['HP'] -= randint(1, 6)


def reset_hp():
    """Reset monster HP.

    A function that resets HP value back to 10 in global character dictionary."""
    global monster
    monster['HP'] = 5


def main():
    pass


if __name__ == "__main__":
    main()
