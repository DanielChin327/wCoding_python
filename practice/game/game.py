def ask_question(question, option1, option2):
    print(question)
    print(f"1: {option1}")
    print(f"2: {option2}")
    while True:
        choice = input("Choose 1 or 2: ")
        if choice == '1':
            return 1
        elif choice == '2':
            return 2
        else:
            print("Invalid choice, please select 1 or 2.")

def start_game():
    while True:
        print("Flowchart game!\n")


        # Question 1
        choice = ask_question("Am I ugly?", "Yes", "No")

        if choice == 1:
            # Question 2a
            choice = ask_question("How Ugly?", "A lot", "A little")

            if choice == 1:
                # Question 3a
                choice = ask_question("Do birds die in the street when they see your face?", "Yes. It gets pretty bad during the summer", "No, they just fly off")

                if choice == 1:
                    print("Result: That's pretty bad...You should wear a mask. You could cause a car accident")
                else:
                    print("Result: You have a chance then. Have some hope. And a mask.")

            else:
                # Question 3b
                choice = ask_question("Has anyone ever mistaken you for the 'before' image in a Korean Plastic Surgery Advertisement?", "Yes, I get model offers a lot", "No, but the images look like my relatives")

                if choice == 1:
                    print("Result: Good news! If coding doesn't work, you have a job as a model in Plastic Surgery Ads.")
                else:
                    print("Result: Donate yourself to modern art.")

        else:
            # Question 2b
            choice = ask_question("Are you sure you're not just denying?", "Yes, I'm sure", "Maybe, I could be in denial")

            if choice == 1:
                # Question 3c
                choice = ask_question("Do you have more personality than looks?", "I think so", "No")

                if choice == 1:
                    print("Result: Drink soju before looking in the mirror. Maybe it will help.")
                else:
                    print("Result: Good. Because you are ugly.")

            else:
                # Question 3d
                choice = ask_question("Do you spend a lot of time convincing yourself you're good-looking?", "Every day", "Nah, I've given up")

                if choice == 1:
                    print("Result: Time is more valuable than that. Please re-evaluate your life decisions.")
                else:
                    print("Result: Honesty is the best policy. And in your case, so are paper bags.")

        print("\nWould you like to try again?")
        retry = input("Enter 'yes' to play again or any other key to exit: ").strip().lower()
        if retry != 'yes':
            print("Thanks for playing! Remember, beauty is subjective... but mostly to other people.")
            break

if __name__ == "__main__":
    start_game()
