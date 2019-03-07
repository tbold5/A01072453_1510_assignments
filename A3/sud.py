"""COMP1510 Assignment # 3: Your First SUD!"""

# Trae Bold
# A01072453
# JAN 11, 2019

import sys
import character
import monster
from random import randint


def print_monster():
    print("""
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/," """)


def print_candy_reward():
    print("""         o   oo                     
     o         o   o                
        ___o o   o                  
       /`._;o       o               
      |   /   o                     
      ;_  |                        
        `-'                       
   Bags of candy$$$          """)


def print_exit():
    print("""
                                                888888b
                                                8888888
                                                8888888
                                                8888888
                                     _          8888888
                                   ,d88         8888888
                            ____  d88' _,,      888888'
                           (8888\ 88' d888)     Y8888P
                           ___~~8 ~8  88~___    d8888
  _______              ,8888888        ~ 888888_8888
,8888888888===__    _,d88P~~               ~~Y88888'
88888888888888888888888'                        `88b
8888888888888888888888P                          Y88
`~888888888888~~~~~ 88                            88
    ~~~~~~~~        88                            88
                    88                            88
                    88                            88
                    88                            88
                    88    ,aa.            ,aa.    88
                    88    d88b            d88b    88
                  ,=88    Y88P            Y88P    88=,
                ,d88P'     `'     _aa_     `'     `Y88b,     ___
                88P'             (8888)             `Y88  ad88888b
                88                ~^^~                88 d88Y~~"Y8b
         _______"Yb._                              _.d8"d8Y      88
 ______,d88888888ba888=,.______________________.,=8888~d88_______88___
|~~~~~~88P~~~~~~Y88~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|      88        88                                                   |
|      88        88    hi,                                            |
|      88ba,___,d8P                                                   |
|       "888888888       Thank you for playing my game!               |
|          ~~~~~~                                                     |
|       Dear Warrior Kitty, your bravery will be acknowledged         | 
|   and I personally would like to thank you for standing up against  |
|   those hideous monsters. The Kingdom of Hershey will always be safe|
|   in your hands.                                                    |
|        It is my first SUD game and I am very grateful that you got  |
|   to play my first ever game!                                       |
|        Please come back again!                                      |
|                                               |\      _,,,--,,_  ,) |
|    Sincrely, Trae Bold                        /,`.-'`'   -,  ;-;;'  |
|_____________________________________________ |,4-  ) )-,_ ) /\______|
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'---''(_/--' (_/-'~~~~~~""")


def print_intro():
    print("""    
           / \                                                       / |
          |  |                                                      |  |
         /----\                  Kingdom of Hershey                /----|
        [______]             Where Happy Kitties Reside          [______]
         |    |         _____                        _____         |    |
         |[]  |        [     ]                      [     ]        |  []|
         |    |       [_______][ ][ ][ ][][ ][ ][ ][_______]       |    |
         |    [ ][ ][ ]|     |  ,----------------,  |     |[ ][ ][ ]    |
         |             |     |/'    ____..____    '\|     |             |
          \  []        |     |    /'    ||    '\    |     |        []  /
           |      []   |     |   |o     ||     o|   |     |  []       |
           |           |  _  |   |     _||_     |   |  _  |           |
           |   []      | (_) |   |    (_||_)    |   | (_) |       []  |
           |           |     |   |     (||)     |   |     |           |
           |           |     |   |      ||      |   |     |           |
         /''           |     |   |o     ||     o|   |     |           ''|
        [_____________[_______]--'------''------'--[_______]_____________]""")


def print_happy_kitty():
    print(""" _   _         _  _          _   __ _
    | | | |  ___  | || |  ___   | | / /(_)  _     _
    | |_| | / _ \ | || | / _ \  | |/ /  _ _| |_ _| |_  _  _
    |  _  |/ /_\ \| || |/ / \ \ |   /  | |_   _|_   _|| |/ /
    | | | |\ ,___/| || |\ \_/ / | |\ \ | | | |_  | |_ | / /
    |_| |_| \___/ |_||_| \___/  |_| \_\|_| \___| \___||  /
                           _           _              / /
                          / \_______ /|_\             \/
                         /          /_/ \__
                        /             \_/ /
                      _|_              |/|_
                      _|_  O    _    O  _|_
                      _|_      (_)      _|_
                       \                 /
                        _\_____________/_
                       |  \/  (___)  \/  |
                       \__(  o     o  )__/
                       """'\n\n')


def print_sad_kitty():
    print(""" _   _         _  _          _   __ _
    | | | |  ___  | || |  ___   | | / /(_)  _     _
    | |_| | / _ \ | || | / _ \  | |/ /  _ _| |_ _| |_  _  _
    |  _  |/ /_\ \| || |/ / \ \ |   /  | |_   _|_   _|| |/ /
    | | | |\ ,___/| || |\ \_/ / | |\ \ | | | |_  | |_ | / /
    |_| |_| \___/ |_||_| \___/  |_| \_\|_| \___| \___||  /
                           _           _              / /
                          / \_______ /|_\             \/
                         /          /_/ \__
                        /             \_/ /
                      _|_              |/|_
                      _|_  X    _    X _|_
                      _|_      (_)      _|_
                       \      _____     /
                        _\_____________/_
                       |  \/  (___)  \/  |
                       \__(  o     o  )__/
                       """'\n\n')


def create_map():
    """Create map to display game map to user."""

    # Create map structure.
    game_map = [['  ' for x in range(8)] for _ in range(8)]

    # Set Character position.
    character_icon = '🐰'
    game_map[character.get_position()[0]][character.get_position()[1]] = character_icon

    # Prints the row of the board
    for row in game_map:
        print(row)

    return game_map


def user_command():
    """Ask user command."""

    try:
        user_input = int(input('Which direction would you like to move?: (1) North / (2) South /'
                               '(3) East / (4) West / (5) Quit: '))
        valid_inputs = [1, 2, 3, 4, 5]
        if user_input not in valid_inputs:
            print('I did not understand you')
        else:
            return user_input

    except ValueError:
        print('*' * 50)
        print('Please provide a number instead of a letter!')
        print('*' * 50)
        user_command()


def check_boundary(user_choice: int):

    if (user_choice == 1 and character.get_position()[0] == 0) \
            or (user_choice == 2 and character.get_position()[0]) == 7:
                print('You have hit the candy wall!')
                return False

    elif (user_choice == 4 and character.get_position()[1] == 0) \
            or (user_choice == 3 and character.get_position()[1] == 7):
                print('You hit the candy wall!')
                return False

    return True


def move_character(user_choice: int, boundary: bool, encounter: bool):

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
            print_exit()
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


def monster_encounter_chance():

    if randint(1, 10) == 1:
        return True


def monster_encounter():

        try:
            if monster_encounter_chance():
                print('You have encountered a monster!!\n')
                print_monster()
                print('\n\n')
                user_choice = int(input('(1) Attack Monster? / (2) Flee?\n').lower())

                if user_choice == 1:
                    combat_to_death()

                elif user_choice == 2:
                    flee_from_monster()

                else:
                    print('Sorry I did not understand you\n\n')
                    monster_encounter()

        except ValueError:
            print('*' * 50)
            print('Please provide a number instead of a letter!')
            print('*' * 50)
            pass


def flee_from_monster():

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

    while character.get_hp() > 0 and monster.get_hp() > 0:
        monster.decrease_hp()
        print(character.get_name(), 'BIT', monster.get_name(), ', ', character.get_name(), 'DEALT DAMAGE',
              ', ', monster.get_name(), "current HP is: ", monster.get_hp())

        if monster.get_hp() <= 0:
            print(character.get_name(), ' successfully ate the monster!\n\n')
            print_candy_reward()
            print('\n\n')
            print(character.get_name(), 'current HP is: ', character.get_hp())

        elif monster.get_hp() > 0:
            character.encounter_decrease_hp()
            print(monster.get_name(), 'BIT', character.get_name(), ', ', monster.get_name(), 'DEALT DAMAGE',
                  ', ', character.get_name(), "current HP is: ", character.get_hp())

            if character.get_hp() <= 0:
                print('You got DIABETES! you lost!')
                sys.exit()


def main():
    print_intro()
    user_choice = 0
    boundary = check_boundary(user_choice)
    encounter = monster_encounter_chance()
    # print_happy_kitty()
    character.set_name()
    create_map()
    while user_choice != 5:
        user_choice = user_command()
        move_character(user_choice, boundary, encounter)
        create_map()


if __name__ == '__main__':
    main()
