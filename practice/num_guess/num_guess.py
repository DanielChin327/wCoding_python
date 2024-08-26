import random

random_num = 0

def set_difficulty(choice):
    if choice == 'easy':
        random_num = random.randint(1, 5)
        return random_num
    elif choice == 'medium':
        random_num = random.randint(1, 10)
        return random_num
    elif choice == 'hard':
        random_num = random.randint(1, 20)
        return random_num
def pick_difficulty():
    while True:
        choice = input("Pick a difficulty: (easy / medium / hard): ")
        choice = choice.lower()
        if choice == 'easy':
            return 'easy'
        elif choice == 'medium':
            return 'medium'
        elif choice == 'hard':
            return 'hard'
        else:
            print("invalid input. please choose easy, medium, or hard")

def start_game():
    counter = 3
    choice = pick_difficulty()
    random_num = set_difficulty(choice)
    while counter > 0:
        guess = input ("Guess a number: ")
        try:
            guess = int(guess)
        except ValueError:
            print(f"Invalid input. You wrote {guess}. Write a number.")
        if guess < random_num:
            counter -= 1
            print(f"Too Low. Chances Left: {counter}")
        elif guess > random_num:
            counter -= 1
            print(f"Too High. Chances Left: {counter}")
        elif guess == random_num:
            print(f"\nYou got it! The number was {random_num}!")
            break
    if counter == 0:
        print(f"You lose! Out of chances! The number was {random_num}")
    again = input("\nPlay again? type 'yes'")
    if again == 'yes':
        start_game()

start_game()
