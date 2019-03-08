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

    # Create a map structure using list comprehension.
    game_map = [['  ' for x in range(8)] for _ in range(8)]

    # Set Character position.
    character_icon = '🐰'
    game_map[character.get_position()[0]][character.get_position()[1]] = character_icon

    # Prints each row of the board
    print("""🍭🍭🍭  MAP OF HERSHEY KINGDOM🏰  🍭🍭🍭""")
    for row in game_map:
        # for column in row:
        #     print(column)
        print(' 🍬 '.join(row))

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


def is_valid_move(user_choice: int):
    """Check map boundary.

    A function that takes user command and returns boolean value and prints helpful message when user reaches
    the map boundary."""

    if user_choice == 1 and character.get_position()[0] == 0:
        print('⛔⛔⛔ You have hit the candy wall! ⛔⛔⛔')
        return False

    if user_choice == 2 and character.get_position()[0] == 7:
        print('⛔⛔⛔ You have hit the candy wall! ⛔⛔⛔')
        return False

    if user_choice == 4 and character.get_position()[1] == 0:
        print('⛔⛔⛔ You hit the candy wall! ⛔⛔⛔')
        return False

    if user_choice == 3 and character.get_position()[1] == 7:
        print('⛔⛔⛔ You hit the candy wall! ⛔⛔⛔')
        return False

    return True


def is_max_health():
    """Check character max health.

    A function that return boolean value depending on character HP."""
    if character.get_hp() == 10:
        return True

    return False


def move_character(user_choice: int, max_hp: bool, valid_move=True):
    """Move Character.

    A function that takes user command and updates character position, takes boolean values to determine
    if user HP increases or not."""
    if is_valid_move(user_choice):

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
            character.save_character()
            sys.exit()
        else:
            print('Invalid input')

            create_map()

    # Increase HP only when character is <= 10 HP and is within the map.
    if not max_hp and valid_move:
        character.increase_hp()

    # monster_encounter()
    # 19-> lines


def is_encounter_monster():
    """Calculate encounter chance.

    A function that returns True value with 10% chance."""

    if randint(1, 2) == 1:
        return True

    return False


def monster_encounter():
    """Encounter monster.

    A function that prompts user to make choice and calls other functions depending on their choice. """
    try:
        if is_encounter_monster():
            print('You have encountered a monster!!\n')
            story.print_monster()
            print('\n\n')
            user_choice = int(input('(1) Attack Monster? / (2) Flee?\n'))

            if user_choice == 1:
                combat_to_death()

            elif user_choice == 2:
                flee_from_monster()

    # Catch Error when user inputs letters.
    except ValueError:
        print('*' * 50)
        print('Please provide a number instead of a letter!')
        print('*' * 50)
        monster_encounter()
        # 18-> lines


def flee_from_monster():
    """Flee monster.

    A function that prints helpful message and updates character HP with 10% chance."""
    if randint(1, 10) == 1:
        character.flee_decrease_hp()
        print('Candy monster struck you while you escaped\r\r')
        print('Your Current HP is: ', character.get_hp())

        if character.get_hp() <= 0:
            print('Your Current HP is: ', character.get_hp())
            print('You died out of DIABETES!\n\n')
    else:
        print('You successfully escaped from the Candy Monster\r\r')


def combat_to_death():
    """Combat to death.

    A function that represents combat to death between the character and the monster using their dictionaries."""

    while character.get_hp() > 0 and monster.get_hp() > 0:
        monster.decrease_hp()
        print(character.get_name(), 'STRUCK', monster.get_name(), ', ', character.get_name(), 'DEALT DAMAGE',
              ', ', monster.get_name(), "current HP is: ", monster.get_hp())

        if monster.get_hp() <= 0:
            print(character.get_name(), ' successfully killed the monster!\n\n')
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
                save_or_no = input('Do you want SWEET revenge?  Y/ N: ').upper()
                if save_or_no == 'Y':
                    character.reset_hp()
                    character.save_character()
                    sys.exit()
                else:
                    pass
    monster.reset_hp()
    # 16-> lines


def main():
    print(is_max_health())
    # Story Introduction (ASCII arts)
    story.print_intro()
    story.print_intro_1()
    story.print_happy_kitty()

    # Assign functions to variables.
    user_choice = 0

    # Loads JSON file and starts game from last saved position.
    ask_user = input('1) New Game? / 2) Continue Game?: ')
    if ask_user == '2':
        character.load_character()
        character.greet_user()
    else:
        character.set_name()
    create_map()

    # Run game until user quits.
    while user_choice != 5:
        user_choice = user_command()
        move_character(user_choice, is_max_health(), is_valid_move(user_choice))
        monster_encounter()
        print('Your  current HP is: ', character.get_hp())
        create_map()


if __name__ == '__main__':
    main()
