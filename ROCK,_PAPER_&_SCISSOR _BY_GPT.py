import random

#define the function which will determine the winner
def determine_winner(player1, player2):
    if player1 == player2:
        return "It's a tie!"
    elif player1 == "rock" and player2 == "scissors":
        return "Player 1 wins!"
    elif player1 == "scissors" and player2 == "paper":
        return "Player 1 wins!"
    elif player1 == "paper" and player2 == "rock":
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

#define the options available to select
choices = ["rock", "paper", "scissors"]

#both players need to input the data from the choices
player1_choice = input("Player 1, enter your choice (rock/paper/scissors): ").lower()
player2_choice = input("Player 2, enter your choice (rock/paper/scissors): ").lower()

#if players does not select from the given choices it will show error
if player1_choice not in choices or player2_choice not in choices:
    print("Invalid choice. Please choose from rock, paper, or scissors.")
else:
    winner = determine_winner(player1_choice, player2_choice)
    print(winner)
