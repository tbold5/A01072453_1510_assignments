import random

def rock_paper_scissors():
    """Play Rock Paper Scissor.

    A function that allows players to play rock paper scissors with the computer.
    PARAM: prompt user to put rock, paper or scissor.
    PRECONDITION: user must put the right input.
    POSTCONDITION: prints out computers choice and lets the player know who won.
    """
    initial_input = str(input("Please choose one of the following: 'ROCK' 'PAPER' or 'SCISSOR': "))
    strip_input = initial_input.strip()
    user_input = strip_input.lower()
    my_list = ['rock', 'paper', 'scissor']

    #Use random module to give random int between 0-2
    random_int = random.randint(0, 2)
    #Use indexing to get random outputs
    computer_input = my_list[random_int]


    if user_input =='rock' and computer_input == 'paper':
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

if __name__== "__main__":
    main()