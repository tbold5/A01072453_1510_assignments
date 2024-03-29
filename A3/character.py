"""COMP1510 Assignment # 3: Your First SUD!"""

# Trae Bold
# A01072453
# JAN 11, 2019


from random import randint
import json

# Character values will be only modified through functions implemented in character module.
character = {'Name': '', 'HP': 10, 'Damage:': 0, 'Position': [0, 0]}


def save_character():
    """Save JSON file.

    A function that converts character dictionary into JSON file and saves it , for the user to continue the game."""
    global character
    filename = 'character.json'
    with open(filename, 'w') as file_object:
        json.dump(character, file_object)


def load_character():
    """Load JSON file.

    A function that loads JSON file to retrieve information about saved character."""
    global character
    filename = 'character.json'
    with open(filename) as file_object:
        character = json.load(file_object)


def get_stored_username():
    """Get stored username if available."""
    filename = 'character.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'character.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username['Name'] + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


def get_name():
    """Gets the name from the dictionary.

    RETURN: NAME, key from the character dictionary."""

    return character['Name']


def set_name():
    """Sets the name for the dictionary.

    A function that prompts user to provide name for the character and modifies character name in global dictionary."""

    global character
    character['Name'] = input('What is your name Kitty?: ').title()


def get_hp():
    """Gets the HP from the dictionary.

    RETURN: HP, key from the character dictionary. """

    return character['HP']


def reset_hp():
    """Reset character HP.

    A function that resets HP value back to 10 in global character dictionary."""

    global character
    character['HP'] = 10


def get_damage():
    """Gets the damage from the dictionary.

    RETURN: damage, key from the character dictionary."""

    return character['Damage']


def set_damage():
    """Sets the damage for the dictionary.

    A function that modifies damage value numbers between 1 - 6 when called."""

    global character
    character['Damage'] = randint(1, 6)


def get_position():
    """Gets the position from the dictionary.

    RETURN: position, key from the character dictionary."""

    return character['Position']


def set_position():
    """Sets the position for the dictionary.

    RETURN: position, key from the character dictionary."""

    global character
    return character['Position']


def increase_hp():
    """Increase HP by one.

    A function that increase character HP value by plus one, and modifies character dictionary."""

    global character
    character['HP'] += 1


def encounter_decrease_hp():
    """Decrease HP by random numbers between 1 - 6.

    A function that decreases character HP value numbers between 1 - 6 when called,
    and modifies character dictionary."""

    global character
    character['HP'] -= randint(1, 6)


def flee_decrease_hp():
    """Decrease HP by random numbers between  1 - 4.

    A function that decreases character HP value numbers between 1 - 4 when called,
    and modifies character dictionary."""

    global character
    character['HP'] -= randint(1, 4)


def main():
    pass


if __name__ == "__main__":
    main()
