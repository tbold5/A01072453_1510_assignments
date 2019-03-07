from random import randint

monster = {'Name': 'Chocolatator', 'HP': 5, 'Damage:': 0}


def get_name():
    """Gets the name from the dictionary."""

    return monster['Name']


def get_hp():
    """Gets the HP from the dictionary."""

    return monster['HP']


def get_damage():
    """Gets the damage from the dictionary."""

    return monster['Damage']


def get_monster():
    """Gets monster keys and values from the dictionary."""
    return monster


def decrease_hp():
    """Decrease HP by random numbers between 1 - 6."""
    global monster
    monster['HP'] -= randint(1, 6)


def main():
    pass


if __name__ == "__main__":
    main()
