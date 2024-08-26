import random


#  random_num = random.randint(0, 2) is for 0 to 2

random_num = 0

def set_difficulty(choice):
    if choice == 'easy':
        random_num = random.randint(0, 5)
        return random_num
    elif choice == 'medium':
        random_num = random.randint(0, 20)
        return random_num
    elif choice == 'hard':
        random_num = random.randint(0, 50)

def pick_difficulty():
    while True:
        choice = input("Pick a difficulty: (easy / medium / hard)")
        choice = choice.lower()
        if choice == 'easy':
            return 'easy'
        elif choice == 'medium':
            return 'medium'
        elif choice == 'hard':
            return 'hard'
        else
            return "invalid input. please choose easy, medium, or hard"
