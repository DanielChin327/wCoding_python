# src/game.py

import random

def comp_choice():
    random_num = random.randint(0, 2)
    choices = ['rock', 'paper', 'scissor']
    return choices[random_num]

def player_choice():
    while True:
        player_choice = input("\nRock, Paper, Scissors! Choose: ")
        player_choice = player_choice.lower()
        if player_choice in ['rock', 'paper', 'scissor']:
            return player_choice
        else:
            print(f"invalid input. You typed {player_choice}. Choose Rock, Paper, or Scissors.")

def check_game(comp_choice, player_choice):
    if comp_choice == player_choice:
        return 'tie'
    elif (comp_choice == 'rock' and player_choice == 'paper') or \
        (comp_choice == 'paper' and player_choice == 'scissor') or \
        (comp_choice == 'scissor' and player_choice == "rock"):
        return "player"
    elif (comp_choice == 'paper' and player_choice == 'rock') or \
        (comp_choice == 'scissor' and player_choice == 'paper') or \
        (comp_choice == 'rock' and player_choice == "scissor"):
        return 'computer'
    else:
        return "Invalid Input"

def start_game():
    # Full implementation here...
    pass

# start_game()  # Keep this commented when testing
