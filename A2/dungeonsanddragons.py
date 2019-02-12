"""COMP1510 Assignment #2"""

# Trae Bold
# A01072453
# JAN 11, 2019

import random


def roll_die(number_of_rolls, number_of_sides):
    """Roll a die.

    A function that simulates rolling die of the specified size and the number of times.
    PARAM: int, number_of_rolls.
    PARAM: int, number_of_sides.
    PRECONDITION: number_of_rolls must be a positive integer or the function returns 0.
    PRECONDITION: number_of_sides must be a positive integer or the function returns 0.
    RETURN: random total of number_of_rolls and random_of_sides.
    """

    result = random.randint(1 * number_of_rolls, number_of_sides * number_of_rolls)
    return result


def choose_inventory(inventory, selection):
    """Create sorted list.

    A function that accepts list  and an integer and return new sorted list.
    PARAM: list, inventory.
    PARAM: int, list.
    POSTCONDITION: when list is empty and selection 0, return empty list.
    POSTCONDITION: prints error when selection is negative and return nothing.
    POSTCONDITION: prints error when selection is greater than list return nothing.
    POSTCONDITION: return copy of the list when selection is equal to the list.
    RETURN: sorted list with randomly selected numbers.
    """
    tools_and_artifacts = ['Potion', 'Clarity', 'Hammer', 'Elixir', 'Axe', 'Bow', 'Blade', 'Shield', 'Spear', 'Wand']
    if inventory == [] and selection == 0:
        return []
    elif len(tools_and_artifacts) < 0:
        print('Number of items to choose must be more than 0!')
        return None
    elif len(tools_and_artifacts) < selection:
        print('Number of items exceeds the item in the list ')
        return None
    elif inventory == selection:
        copy_inventory = inventory[:]
        return copy_inventory
    else:
        my_sample = random.sample(tools_and_artifacts, selection)
        my_sample.sort()
        return my_sample


def create_character(name_length):
    """Create a Character.

    A function that create a Dungeon and Dragons character.
    PARAM: name_length, a positive int
    PRECONDITION: name_length must be positive
    RETURN: a correctly created D&D character in a list
    """
    if name_length < 0:
        print('Name length can not be a negative number!')
        return None
    else:

        my_character = {}
        my_character['Name'] = generate_name(name_length)
        my_character['Class'] = class_creator().lower()
        my_character['HP'] = 5 * roll_die(1, class_dictionary()[my_character['Class']])
        my_character['Strength'] = roll_die(3, 6)
        my_character['Dexterity'] = roll_die(3, 6)
        my_character['Constitution'] = roll_die(3, 6)
        my_character['Intelligence'] = roll_die(3, 6)
        my_character['Wisdom'] = roll_die(3, 6)
        my_character['Charisma'] = roll_die(3, 6)
        my_character['XP'] = 0
        my_character['Inventory'] \
            = choose_inventory(0, int(input('Choose number of items between 1 - 9 to fight the Dragon!: ')))

        return my_character


def print_character(character):
    """Print character.

    A function that prints create character function.
    PARAM: list, character
    """
    return create_character(character)


def generate_name(syllable_length):
    """Generate name.

    A function that generates syllables consisting consoanant followed by vowels.
    PARAM: syllables, a positive integer.
    PRECONDITION: syllables must be positive non-zero integers.
    POSTCONDITION: syllable must consist consonant followed by vowels.
    RETURN:
    """
    syllable = ''

    for i in range(syllable_length):
        syllable += generate_syllable()
    return syllable.title()


def generate_vowel():
    """Generate vowel.

    A function that generates vowel including y.
    RETURN: single vowel.
    """
    vowels = "aeiouy"
    random_vowels = random.choice(vowels)
    return random_vowels


def generate_consonant():
    """Generate consonant.

    A function that generates consonant including y.
    RETURN: single consonant.
    """
    consonant = "bcdfghjklmnpqrstvxzwy"
    random_consonant = random.choice(consonant)
    return random_consonant


def generate_syllable():
    """Generate syllable.

    A function that creates syllable using generate_consonant and generate_vowel functions.
    RETURN: concatenated syllable consisting consonant followed by vowel.
    """
    random_syllable = generate_consonant() + generate_vowel()
    return random_syllable


def class_creator():
    """Print character classes.

    A function that prints out all possbile character classes for user to choose.
    """
    class_list = {'Barbarian': 12, 'Bard': 8, 'Cleric': 8, 'Druid': 8, 'Fighter': 10, 'Monk': 8, 'Paladin': 10,
                  'Ranger': 10, 'Rogue': 8, 'Sorcerer': 6, 'Warlock': 8, 'Wizard': 6, 'Blood Hunter': 10}
    print(class_list)
    user_class = input('Please choose your character class from the following list: ').title()

    if user_class not in class_list:
        return 'Please Choose Character Class from the list!'
    else:
        return user_class


def class_dictionary():
    """Return Class Dictionary.

    A function that returns dictionary of character classes.
    RETURN: character class dictionary.
    """
    class_list = {'barbarian': 12, 'bard': 8, 'cleric': 8, 'druid': 8, 'fighter': 10, 'monk': 8, 'paladin': 10,
                  'ranger': 10, 'rogue': 8, 'sorcerer': 6, 'warlock': 8, 'wizard': 6, 'blood Hunter': 10}
    return class_list


def first_striker():
    """Determine first striker

    A function that decides which player to attack first by rolling out two random numbers between 1 - 20.
    RETURN: returns True value when opponent_1 is more than opponent_2, else False.
    """
    opponent_1 = roll_die(1, 20)
    opponent_2 = roll_die(1, 20)

    if opponent_1 == opponent_2:
        first_striker()
    elif opponent_1 > opponent_2:
        return True
    else:
        return False


def combat_round(opponent_one, opponent_two):
    """Fight characters.

    A function that represents single round of combat between two characters using their dictionaries.
    PARAM: opponent_one, correctly implemented dictionary.
    PARAM: opponent_two, correctly implemented dictionary.
    PRECONDITION: opponent_one, dictionary containing correct character.
    PRECONDITION: opponent_two, dictionary containing correct character.
    """
    if first_striker():
        attacker = opponent_one
        defender = opponent_two
    else:
        attacker = opponent_two
        defender = opponent_one

    if roll_die(1, 20) > defender['Dexterity']:
        damage = roll_die(1, class_dictionary()[attacker['Class']])
        defender['HP'] -= damage
        print(attacker['Name'], 'attacked ', defender['Name'], ', ', defender['Name'], "current HP is: ", defender['HP'])
        if defender['HP'] <= 0:
            print(defender['Name'], 'is dead!', attacker['Name'], 'is the winner!')
    else:
        print(attacker['Name'], " missed the attack!")

    if defender['HP'] > 0:
        if roll_die(1, 20) > attacker['Dexterity']:
            damage = roll_die(1, class_dictionary()[defender['Class']])
            attacker['HP'] -= damage
            print(defender['Name'], 'attacked ', attacker['Name'], ', ', attacker['Name'], 'current HP is: ',
                  attacker['HP'])
            if attacker['HP'] <= 0:
                print(attacker['Name'], 'is dead!', defender['Name'], 'is the winner!')
        else:
            print(defender['Name'], " missed the attack!")


def main():
    player_1 = create_character(2)
    player_2 = create_character(4)
    print(player_1)
    print(player_2)
    while player_1['HP'] > 0 and player_2['HP'] > 0:
        combat_round(player_1, player_2)


if __name__ == "__main__":
    main()

