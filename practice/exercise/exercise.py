import random




while True:
    number = random.randint(1,20)
    attempt = 0
    while True:
        guess = input("Guess the number: ")
        guess = int(guess)
        if guess == number:
            attempt += 1
            print(f"You got it! the number is {number}")
            print(f"You made {attempt} attempts")
            quit = input(f"Press any key to continue (type 'quit' to stop)")
            if quit == "quit":
                break
            else:
                number = random.randint(1,20)
                attempt = 0
        elif guess < number:
            attempt += 1
            print("Too low...")
        elif guess > number:
            attempt += 1
            print("Too high...")
