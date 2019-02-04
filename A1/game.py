"""COMP 1510 Assignment 1: Rock Paper Scissors!"""

# Trae Bold
# A01072453
# Feb 03, 2019

import random


def rock_paper_scissors():
    """Play Rock Paper Scissor.

    A function that allows players to play rock paper scissors with the computer.
    Prompts user to put rock, paper or scissor.
    PARAM: N/A
    PRECONDITION: user must only input 'rock' 'paper' 'scissor' as a string.
    POSTCONDITION: prints out computers choice and lets the player know who won.
    RETURN: N/A
    """
    initial_input = str(input("Please choose one of the following: 'ROCK' 'PAPER' or 'SCISSOR': "))
    strip_input = initial_input.strip()
    user_input = strip_input.lower()

    game_generator(user_input)


def game_generator(user_input):
    """Generate Rock, Paper, Scissor

    A function that generates rock paper scissors and compares with user input to decide the outcome..
    Prompts user to put rock, paper or scissor.
    PARAM: str, input from user from 'rock', 'paper', 'scissor'.
    PRECONDITION: user must only input 'rock' 'paper' 'scissor' as a string.
    POSTCONDITION: prints out computers choice and lets the player know who won.
    RETURN: N/A
    """

    my_list = ['rock', 'paper', 'scissor']
    random_int = random.randint(0, 2)
    computer_input = my_list[random_int]

    if user_input == 'rock' and computer_input == 'paper':
        print("The computer choose PAPER: YOU LOSE")
    elif user_input == 'rock' and computer_input == 'scissor':
        print("The computer choose SCISSOR: YOU WIN")
    elif user_input == 'scissor' and computer_input == 'rock':
        print("The computer choose ROCK: YOU LOSE")
    elif user_input == 'scissor' and computer_input == 'paper':
        print("The computer choose PAPER: YOU WIN")
    elif user_input == 'paper' and computer_input == 'rock':
        print("The computer choose ROCK: YOU WIN")
    elif user_input == 'paper' and computer_input == 'scissor':
        print("The computer choose SCISSOR: YOU LOSE")
    elif user_input == computer_input:
        print('The computer choose: ' + computer_input.upper() + ' , IT`S A TIE!')
    else:
        print("You did not pick the right input, choose from 'ROCK' 'PAPER' 'SCISSOR'")


def main():
    rock_paper_scissors()


if __name__ == "__main__":
    main()
