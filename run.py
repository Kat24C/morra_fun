import random


def user_details():
    """
    The user enter his/her name
    As well as a breakdown of the rules of the game.
    """
    name = (input("What is your name? \n")).strip()
    print(f"Hello,{name} are you ready to play a game of morra.")
    print("In this game you need to guess the computers number.")
    print("While the computer guesses your number.")
    print("You have to choose between 1, 2 and 3. ")
    print('The first person to reach 12 wins.')
    print()
    game_choice()

user_details()


def game_choice():
    """
    Here we are going to ask the user to input a number
    between 1 and 3. 
    The computer will randomize a number between 1 and 3. 
    Then we will compare the two numbers to see if they 
    are the same or different. 
    """


def finalgame(player_score, comp_score):
    """
    Here we will compare the scores and see if the game continues.
    It will see if the computer or user has scored 12 or more.
    It will declare a winner once user or computer score 12.
    """


def play_again():
    """
    Asks the user if they would like to restart the game.
    The user will have the option to restart or end the game. 
    """


