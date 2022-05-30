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


def game_choice():
    """
    Here we are going to ask the user to input a number
    between 1 and 3.
    The computer will randomize a number between 1 and 3.
    Then we will compare the two numbers to see if they
    are the same or different.
    """
    player_score = 0
    comp_score = 0
    while True:
        try:
            user_choice = int(input("Choose a number between 1 and 3: "))
            while user_choice != 1 or user_choice != 2 or user_choice != 3:
                if user_choice == 1 or user_choice == 2 or user_choice == 3:
                    break
                else:
                    print("Please enter a valid number")
        except ValueError:
            print("Please enter a valid number")
            user_choice = int(input("Choose a number between 1 and 3: "))
            while user_choice != 1 or user_choice != 2 or user_choice != 3:
                if user_choice == 1 or user_choice == 2 or user_choice == 3:
                    break
                else:
                    print("Please enter a number between 1 and 3.")
                    user_choice = int(input("\
Choose a number between 1 and 3: "))

        computer_guess = random.randint(1, 3)
        print(f"The computer chose: {computer_guess}\n")


        if user_guess == computer_choice:
            user_score = user_guess + computer_choice
            print(f"Well done, You got {user_score}")
            player_score = player_score + user_score
            print(f"Your total is {player_score}\n")
        else:
            print("Oh dear, try again you got 0")
            print(f"Your total is {player_score}")

        if user_choice == computer_guess:
            computer_score = user_choice + computer_guess
            print(f"The computer got {computer_score}")
            comp_score = comp_score + computer_score
            print(f"The computer's total is {comp_score}\n")
        else:
            print("The computer got 0")
            print(f"The computer's total is {comp_score}\n")
            finalgame(player_score, comp_score)


user_details()