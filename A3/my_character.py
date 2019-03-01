import random


def kitty_character():
    kitty_character_dic = {'HP': 10, 'Damage': roll_die(1, 6), 'x': 2, 'y': 0}
    kitty_character_dic['Name'] = input('Please choose a name for you Hello Kitty:  ').title()
    return kitty_character_dic







def main():
    print(create_character())


if __name__ == "__main__":
    main()