import random

def comp_choice():
    random_num = random.randint(0, 2)
    choices = ['rock', 'paper', 'scissor']
    comp_choice = choices[random_num]
    return comp_choice


def player_choice():
    while True:
        player_choice = input("\nRock, Paper, Scissors! Choose: ")
        player_choice = player_choice.lower()
        if player_choice == 'rock':
            return 'rock'
        elif player_choice == 'paper':
            return 'paper'
        elif player_choice == 'scissor':
            return 'scissor'
        else:
            print(f"invalid input. You typed {player_choice}. Choose Rock, Paper, or Scissors.")

def check_game(comp_choice, player_choice):
    if comp_choice == player_choice:
        return 'tie'
    elif (comp_choice == 'rock' and player_choice == 'paper') or (comp_choice == 'paper' and player_choice =='scissor') or (comp_choice == 'scissor' and player_choice == "rock"):
        return "player"
    elif (comp_choice == 'paper' and player_choice == 'rock') or (comp_choice == 'scissor' and player_choice =='paper') or (comp_choice == 'rock' and player_choice == "scissor"):
        return 'computer'
    else:
        return "Invalid Input"



def start_game():
    rounds = input("Play until someone wins to:  ")
    try:
        rounds = int(rounds)
    except ValueError:
        print(f"Invalid input. You wrote {rounds}. Write a number.")
    counter = 0
    player_wins = 0
    computer_wins = 0
    while counter <= rounds:
        computer = comp_choice()
        player = player_choice()
        winner = check_game(computer, player)
        if winner == 'tie':
            print(f"Tie! Both chose {computer}\n")
        elif winner == 'player':
            print(f"Player wins! Player chose {player}. Computer chose {computer}.\n")
            player_wins += 1
            counter += 1
        elif winner == 'computer':
            print((f"Computer wins! Player chose {player}. Computer chose {computer}.\n"))
            computer_wins += 1
            counter += 1
    print(f"RESULTS\nPlayer Score: {player_wins}\nComputer Score: {computer_wins}\n")

    again = input("Type yes to play again: ")
    if again == "yes":
        counter = 0
        start_game()

start_game()
