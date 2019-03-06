"""COMP1510 Assignment # 3: Your First SUD!"""

# Trae Bold
# A01072453
# JAN 11, 2019

import random
import sys
import copy
import my_character





def candy_monster():
    chocolate_monster = {'HP': 5, 'Damage': roll_die(1, 6), 'x': 1, 'y': 2, 'Name': 'ChocoMonsta'}
    return chocolate_monster


def flee_from_monster(character_dic):
    if roll_die(1, 10) == 1:
        character_dic['HP'] -= 1
        print('Candy monster bit you while you escaped')
        print('Your Current HP is: ', character_dic['HP'])
        return character_dic
    else:
        character_dic['HP'] += 0
        print('You successfully escaped from the Candy Monster')
        return character_dic


def monster_encounter_chance():
    if random.randint(1, 2) == 1:
        return True


def monster_encounter(character_dictionary, monster_dictionary):
        if monster_encounter_chance():
            print('You have encountered a monster :O')
            user_choice = input('(a) Attack Monster? / (b) Flee?').lower()
            if user_choice == 'a':
                combat_to_death(character_dictionary, monster_dictionary)
            elif user_choice == 'b':
                flee_from_monster(character_dictionary)
            else:
                print('Sorry I did not understand you')


def combat_to_death(kitty, monster):
        while kitty['HP'] > 0 and monster['HP'] > 0:
            damage = roll_die(1, 6)
            monster['HP'] -= damage
            print(kitty['Name'], 'BIT', monster['Name'], ', ', kitty['Name'], 'DEALT:', damage, 'DAMAGE',
                  ', ', monster['Name'], "current HP is: ", monster['HP'])
            if monster['HP'] <= 0:
                print(kitty['Name'], ' successfully ate the monster!')
            elif monster['HP'] > 0:
                damage = roll_die(1, 6)
                kitty['HP'] -= damage
                print(monster['Name'], 'BIT', kitty['Name'], ', ', monster['Name'], 'DEALT:', damage, 'DAMAGE',
                      ', ', kitty['Name'], "current HP is: ", kitty['HP'])
            if kitty['HP'] <= 0:
                print('You got DIABETES! you lost!')


def main():
    player_dictionary = kitty_character()
    monster_dictionary = candy_monster()
    game_map = create_map()
    print('Welcome to my Kitty World!\n')
    print('1.) Start')
    print('2.) Quit')
    option = input('->')
    if option == '1':
        start(player_dictionary)
    elif option == '2':
        sys.exit()
    else:
        print('Please choose a valid number!')
        main()
    user_input = 0
    while user_input != 5:
        user_input = user_command()
        print_map(game_map, character_new_location(player_dictionary, monster_dictionary, user_input))


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


def start(player_dictionary):
    # os.system('clear')
    print_happy_kitty()
    print('Hello what is your name?')
    option = input('-->').title()
    player_dictionary['Name'] = option
    start1(player_dictionary)


def start1(player_dictionary):
    # os.system('clear')
    player_name = player_dictionary['Name']
    player_damage = player_dictionary['Damage']
    player_HP = player_dictionary['HP']
    print('Hello %s, Welcome to the Candy Land!' % player_name)
    print('--------------------')
    print('Name: %s' % player_name)
    print('Attack: %d' % player_damage)
    print('HP: %d' % player_HP)
    print('1.) Move')
    print('2.) Exit')
    option = input('-->')
    if option == '1':
        move()
    elif option == '2':
        print('Thank you for playing!')
        sys.exit()
    else:
        print('I did not understand that command')
        start1(player_dictionary)


def create_map():
    game_map = [['@' for x in range(3)] for i in range(3)]
    return game_map


def print_map(game_map: list, character_dictionary: dict):
    copy_map = copy.deepcopy(game_map)
    character_position = character_dictionary['Position']
    copy_map[character_position[0]][character_position[1]] = 'X'
    for x in copy_map:
        print(x)
        print('\r')
    # print(character_position)


def user_command():
    user_input = int(input('Which direction would you like to move?: 1) north 2) south'
                           '3) east 4) west 5) quit'))
    valid_inputs = [1, 2, 3, 4, 5]
    if user_input not in valid_inputs:
        print('Choose valid input')
    else:
        return user_input


def check_boundary(character_dictionary: dict, user_choice: int):
    if (user_choice == 1 and character_dictionary['Position'][0] == 0) \
            or (user_choice == 2 and character_dictionary['Position'][0]) == 2:
                print('You have hit the candy wall!')
                return False
    elif (user_choice == 4 and character_dictionary['Position'][1] == 0) \
            or (user_choice == 3 and character_dictionary['Position'][1] == 2):
                print('You hit the candy wall!')
                return False

    return True


def character_new_location(character_dictionary: dict, monster_dictionary: dict, user_choice: int):
    if check_boundary(character_dictionary, user_choice):
        if user_choice == 1:
            character_dictionary['Position'][0] -= 1
            monster_encounter(character_dictionary, monster_dictionary)
        elif user_choice == 2:
            character_dictionary['Position'][0] += 1
            monster_encounter(character_dictionary, monster_dictionary)
        elif user_choice == 3:
            character_dictionary['Position'][1] += 1
            monster_encounter(character_dictionary, monster_dictionary)
        elif user_choice == 4:
            character_dictionary['Position'][1] -= 1
            monster_encounter(character_dictionary, monster_dictionary)
        elif user_choice == 5:
            print('Thank you for playing')
            sys.exit()
        else:
            print('Invalid input')
    return character_dictionary


def move():
    pass


if __name__ == "__main__":
    main()
