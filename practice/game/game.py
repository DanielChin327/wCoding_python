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
        print("Welcome to the Hogwarts House Sorting Quiz!\n")

        # Question 1
        choice = ask_question("You're at a feast, what do you do first?",
                              "Pile your plate high with all the best food",
                              "Make sure everyone else has food before serving yourself")

        if choice == 1:
            # Question 2a
            choice = ask_question("A classmate asks to copy your homework. How do you respond?",
                                  "Sure, anything to help a friend!",
                                  "No way, do your own work!")

            if choice == 1:
                # Question 3a
                choice = ask_question("You find a mysterious book in the Restricted Section. What do you do?",
                                      "Read it immediately",
                                      "Return it to its proper place")

                if choice == 1:
                    # Question 4a
                    choice = ask_question("Do you believe rules are meant to be broken?",
                                          "Yes, they're just guidelines anyway",
                                          "No, rules exist for a reason")

                    if choice == 1:
                        print("Result: You belong in Gryffindor! Brave, bold, and always ready for an adventure.")
                    else:
                        print("Result: You belong in Hufflepuff! Loyal, kind, and always doing what's right.")

                else:
                    # Question 4b
                    choice = ask_question("You see someone being bullied, what do you do?",
                                          "Stand up for them immediately",
                                          "Report it to a teacher")

                    if choice == 1:
                        print("Result: You belong in Gryffindor! Courageous and always ready to defend others.")
                    else:
                        print("Result: You belong in Hufflepuff! Your loyalty to doing the right thing is unmatched.")

            else:
                # Question 3b
                choice = ask_question("You're given the chance to learn any magical skill instantly. What do you choose?",
                                      "Mastering the Patronus Charm",
                                      "Becoming an Animagus")

                if choice == 1:
                    # Question 4c
                    choice = ask_question("Do you prefer working alone or in a team?",
                                          "Alone, I work better that way",
                                          "In a team, we can accomplish more together")

                    if choice == 1:
                        print("Result: You belong in Ravenclaw! Wise and independent, always seeking knowledge.")
                    else:
                        print("Result: You belong in Hufflepuff! A true team player, always looking out for others.")

                else:
                    # Question 4d
                    choice = ask_question("You're in a duel. What's your first move?",
                                          "Expelliarmus!",
                                          "Stupefy!")

                    if choice == 1:
                        print("Result: You belong in Gryffindor! Quick to act and always ready to disarm your opponents.")
                    else:
                        print("Result: You belong in Slytherin! You know how to incapacitate your enemies swiftly.")

        else:
            # Question 2b
            choice = ask_question("You're late to class and a prefect stops you. What do you do?",
                                  "Tell them the truth",
                                  "Make up a believable excuse")

            if choice == 1:
                # Question 3c
                choice = ask_question("You find a secret passage in Hogwarts. Do you:",
                                      "Explore it right away",
                                      "Tell a teacher about it")

                if choice == 1:
                    # Question 4e
                    choice = ask_question("You're offered a powerful, but dark magical artifact. Do you accept it?",
                                          "Yes, power is worth the risk",
                                          "No, it's not worth the danger")

                    if choice == 1:
                        print("Result: You belong in Slytherin! Ambitious and willing to take risks for power.")
                    else:
                        print("Result: You belong in Ravenclaw! Wise enough to know some risks aren't worth taking.")

                else:
                    # Question 4f
                    choice = ask_question("Do you prefer theory or practical magic?",
                                          "Theory, I love understanding the how and why",
                                          "Practical, I want to get my hands dirty")

                    if choice == 1:
                        print("Result: You belong in Ravenclaw! Always curious and eager to learn the deeper truths.")
                    else:
                        print("Result: You belong in Hufflepuff! Hard-working and always ready to put your skills to the test.")

            else:
                # Question 3d
                choice = ask_question("You accidentally brew a potion that turns your skin green. What do you do?",
                                      "Laugh it off, accidents happen",
                                      "Panic and try to fix it immediately")

                if choice == 1:
                    # Question 4g
                    choice = ask_question("Do you enjoy breaking the rules?",
                                          "Sometimes, it's fun",
                                          "Never, I follow them to the letter")

                    if choice == 1:
                        print("Result: You belong in Gryffindor! Adventurous and not afraid to bend the rules.")
                    else:
                        print("Result: You belong in Ravenclaw! Disciplined and always in control.")

                else:
                    # Question 4h
                    choice = ask_question("You catch someone sneaking into the Forbidden Forest. Do you:",
                                          "Join them, it sounds exciting",
                                          "Report them to a teacher")

                    if choice == 1:
                        print("Result: You belong in Slytherin! You're not afraid of a little danger.")
                    else:
                        print("Result: You belong in Hufflepuff! You know it's better to play it safe.")

        # Humorous Branch: Disqualification
        print("\nWait a minute... We have one more question.")
        choice = ask_question("Do you own a wand?",
                              "Yes, of course!",
                              "Wait, you need a wand to join Hogwarts?")

        if choice == 2:
            print("\nResult: Sorry, you're not qualified to join Hogwarts. Perhaps try a Muggle school instead.")
        else:
            print("\nResult: Congratulations, you qualify to join Hogwarts! Just don't forget your wand next time.")

        print("\nWould you like to try again?")
        retry = input("Enter 'yes' to play again or any other key to exit: ").strip().lower()
        if retry != 'yes':
            print("Thanks for playing! Remember, Hogwarts is always looking for new students... if you're qualified.")
            break

if __name__ == "__main__":
    start_game()
