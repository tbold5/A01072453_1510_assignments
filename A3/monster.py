from random import randint

monster = {'Name': 'Chocolatator', 'HP': 5, 'Damage:': 0}


def get_name():
    """Gets the name from the dictionary."""

    return monster['Name']


def get_damage():
    """Gets the damage from the dictionary."""

    return monster['Damage']


def set_encounter_damage():
    """Sets the encounter damage for the dictionary."""

    global monster
    monster['Damage'] = randint(1, 6)


def set_flee_damage():
    """Sets the flee damage for the dictionary."""

    global monster
    monster['Damage'] = randint(1, 4)


def get_monster():
    """Gets monster keys and values from the dictionary."""
    return monster


def main():
    pass


if __name__ == "__main__":
    main()
