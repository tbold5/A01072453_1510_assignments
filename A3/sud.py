"""COMP1510 Assignment # 3: Your First SUD!"""

# Trae Bold
# A01072453
# JAN 11, 2019

import sys
import character
import monster
import story
from random import randint


def create_map():
    """Display game map.

    A function that creates game map and displays it to user to
    show their current location."""

    # Create map structure.
    game_map = [['  ' for x in range(8)] for _ in range(8)]

    # Set Character position.
    character_icon = '🐰'
    game_map[character.get_position()[0]][character.get_position()[1]] = character_icon

    # Prints the row of the board
    print("""🍭🍭🍭  MAP OF HERSHEY KINGDOM🏰  🍭🍭🍭""")
    for row in game_map:

        print(row)

    return game_map


def user_command():
    """Ask user command.

    A function that prompts users for command and returns the number corresponding to that command."""

    try:
        user_input = int(input('Which direction would you like to move?: (1) North / (2) South /'
                               '(3) East / (4) West / (5) Quit: '))
        valid_inputs = [1, 2, 3, 4, 5]
        if user_input not in valid_inputs:
            print('I did not understand you')
        else:
            return user_input
    # Catch Value error when user inputs letters.
    except ValueError:
        print('*' * 50)
        print('Please provide a number instead of a letter!')
        print('*' * 50)
        user_command()


def check_boundary(user_choice: int):
    """Check map boundary.

    A function that takes user command and returns boolean value and prints helpful message when user reaches
    the map boundary."""

    if (user_choice == 1 and character.get_position()[0] == 0) \
            or (user_choice == 2 and character.get_position()[0]) == 7:
                print('⛔⛔⛔ You have hit the candy wall! ⛔⛔⛔')
                return False

    elif (user_choice == 4 and character.get_position()[1] == 0) \
            or (user_choice == 3 and character.get_position()[1] == 7):
                print('⛔⛔⛔ You hit the candy wall! ⛔⛔⛔')
                return False

    return True


def move_character(user_choice: int, boundary: bool, encounter: bool):
    """Move Character.

    A function that takes user command and updates character position, takes boolean values to determine
    if user HP increases or not."""
    if check_boundary(user_choice):

        if user_choice == 1:
            character.set_position()[0] -= 1

        elif user_choice == 2:
            character.set_position()[0] += 1

        elif user_choice == 3:
            character.set_position()[1] += 1

        elif user_choice == 4:
            character.set_position()[1] -= 1

        elif user_choice == 5:
            story.print_exit()
            print('Thank you for playing\n\n')
            sys.exit()
        else:
            print('Invalid input')

            create_map()
    if (boundary is False) and (encounter is False):
        character.increase_hp()
    else:
        None

    monster_encounter()
    # 19-> lines


def monster_encounter_chance():
    """Calculate encounter chance.

    A function that returns True value with 10% chance."""

    if randint(1, 10) == 1:
        return True


def monster_encounter():
    """Encounter monster.

    A function that prompts user to make choice and calls other functions depending on their choice. """
    try:
        if monster_encounter_chance():
            print('You have encountered a monster!!\n')
            story.print_monster()
            print('\n\n')
            user_choice = int(input('(1) Attack Monster? / (2) Flee?\n').lower())

            if user_choice == 1:
                combat_to_death()

            elif user_choice == 2:
                flee_from_monster()

            else:
                print('Sorry I did not understand you\n\n')
                monster_encounter()
    # Catch Error when user inputs letters.
    except ValueError:
        print('*' * 50)
        print('Please provide a number instead of a letter!')
        print('*' * 50)
        pass
        # 18-> lines


def flee_from_monster():
    """Flee monster.

    A function that prints helpful message and updates character HP with 10% chance."""
    if randint(1, 10) == 1:
        character.flee_decrease_hp()
        print('Candy monster bit you while you escaped\r\r')
        print('Your Current HP is: ', character.get_hp())

        if character.get_hp() <= 0:
            print('Your Current HP is: ', character.get_hp())
            print('You died out of DIABETES\n\n!')
    else:
        print('You successfully escaped from the Candy Monster\r\r')


def combat_to_death():
    """Combat to death.

    A function that represents combat to death between the character and the monster using their dictionaries."""

    while character.get_hp() > 0 and monster.get_hp() > 0:
        monster.decrease_hp()
        print(character.get_name(), 'BIT', monster.get_name(), ', ', character.get_name(), 'DEALT DAMAGE',
              ', ', monster.get_name(), "current HP is: ", monster.get_hp())

        if monster.get_hp() <= 0:
            print(character.get_name(), ' successfully ate the monster!\n\n')
            story.print_candy_reward()
            print('\n\n')
            print(character.get_name(), 'current HP is: ', character.get_hp())

        elif monster.get_hp() > 0:
            character.encounter_decrease_hp()
            print(monster.get_name(), 'BIT', character.get_name(), ', ', monster.get_name(), 'DEALT DAMAGE',
                  ', ', character.get_name(), "current HP is: ", character.get_hp())

            if character.get_hp() <= 0:
                story.print_death()
                print('You got DIABETES! you lost!')
                sys.exit()
    # 16-> lines


def main():
    story.print_intro()
    story.print_intro_1()
    story.print_happy_kitty()
    user_choice = 0
    boundary = check_boundary(user_choice)
    encounter = monster_encounter_chance()
    character.set_name()
    create_map()
    while user_choice != 5:
        user_choice = user_command()
        move_character(user_choice, boundary, encounter)
        create_map()


if __name__ == '__main__':
    main()
