"""COMP1510 Assignment # 3: Your First SUD!"""

# Trae Bold
# A01072453
# JAN 11, 2019


from random import randint

character = {'Name': '', 'HP': 10, 'Damage:': 0, 'Position': [0, 0]}


def get_name():
    """Gets the name from the dictionary."""

    return character['Name']


def set_name():
    """Sets the name for the dictionary."""

    global character
    character['Name'] = input('What is your name Kitty?: ').title()


def get_hp():
    """Gets the HP from the dictionary."""

    return character['HP']


def get_damage():
    """Gets the damage from the dictionary."""

    return character['Damage']


def set_damage():
    """Sets the damage for the dictionary."""

    global character
    character['Damage'] = randint(1, 6)


def get_position():
    """Gets the position from the dictionary."""

    return character['Position']


def set_position():
    """Sets the position for the dictionary."""

    global character
    return character['Position']


def get_character():
    """Gets character keys and values from the dictionary."""
    return character


def increase_hp():
    """Increase HP by one."""

    global character
    character['HP'] += 1


def encounter_decrease_hp():
    """Decrease HP by random numbers between 1 - 6."""

    global character
    character['HP'] -= randint(1, 6)


def flee_decrease_hp():
    """Decrease HP by random numbers between  1 - 4."""

    global character
    character['HP'] -= randint(1, 4)


def main():
    pass


if __name__ == "__main__":
    main()
