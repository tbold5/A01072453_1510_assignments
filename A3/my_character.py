from random import randint

character = {'Name': '', 'HP': 0, 'Damage:': 0, 'Position': [0, 0]}


def get_name():
    """Gets the name from the dictionary."""

    return character['Name']


def set_name():
    """Sets the name for the dictionary."""

    global character
    character['Name'] = input('What is your name?: ')


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


def set_position(position):
    """Sets the position for the dictionary."""

    global my_character
    character['Position'] = position


def get_character():
    """Gets character keys and values from the dictionary."""
    return character


def main():
    pass


if __name__ == "__main__":
    main()
