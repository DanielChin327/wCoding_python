# Dealer is dealt two cards. One is face up. The other is face down.
# The User is then dealt two cards.
# The game can no longer be played if the user runds out of tokens.
# Starting amount of tokens is 20.
# Can either bet double or fold to

import random
cards = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
wallet = 20

def deal_hand():
    hand = []
    random_num = random.randint(0, 12)
    random_num2 = random.randint(0, 12)
    card1 = cards[random_num]
    card2 = cards[random_num2]
    hand.append(card1)
    hand.append(card2)
    return hand

def draw_again(hand):
    random_num =random.randint(0, 12)
    card = cards[random_num]
    hand.append(card)
    return hand


def convert_card_value(cards):
    converted_cards = []
    for card in cards:
        if type(card) == int:
            converted_cards.append(card)
        elif card == 'J'or card == 'Q' or card == 'K':
            converted_cards.append(10)
        elif card == 'A':
            converted_cards.append(11)
    return converted_cards

def place_bets():
    global wallet
    while True:
        amount = input("Place amount to bet: ")
        try:
            amount = int(amount)
            break
        except:
            print("invalid input. Write a number")
    if amount <= wallet:
        wallet = wallet - amount
        bet = amount
        print(f"Funds: {wallet} \nBet Amount: {bet}\n")
        return bet
    elif amount > wallet:
        print("Insufficent funds...")


def user_hand():
    user_hand = deal_hand()
    while True:
        print(f"Your hand is {user_hand}")
        card_values = convert_card_value(user_hand)
        total = sum(card_values)
        if total > 21:
            print("Bust! You Lose!")
            print(f"funds: {wallet}")
            break
        while True:
            draw = input("draw again? (y/n): ")
            if draw == 'y':
                user_hand = draw_again(user_hand)
                break
            elif draw == 'n':
                return user_hand
            else:
                print("invalid input. type either y / n")


def play_game():
    global wallet
    print("Lets Play BlackJack")
    print("--------------------")
    print("Objective: Try to get a fund of 100")
    print(f"Current Funds: {wallet}")
    while True:
        print("Place a Bet")
        bet = place_bets()
        print("Dealer deals hand")
        dealer_hand = deal_hand()
        print(f"Dealer Hand is [{dealer_hand[0]}, Face_Down]")
        user_cards = user_hand()
        if user_cards != None:
            dealer_hand_value = sum(convert_card_value(dealer_hand))
            user_hand_value = sum(convert_card_value(user_cards))
            if (dealer_hand_value == user_hand_value):
                print("\nTIE")
                print(f"Dealer Hand was {dealer_hand}")
                print(f"Player Hand was {user_cards}")
                wallet = wallet + bet
                break
            elif(dealer_hand_value > user_hand_value):
                print("\nDealer wins!")
                print(f"Dealer Hand was {dealer_hand}")
                print(f"Player Hand was {user_cards}")
                break
            elif(dealer_hand_value < user_hand_value):
                print(f"\nPlayer Wins! Player Wins {bet}")
                print(f"Dealer Hand was {dealer_hand}")
                print(f"Player Hand was {user_cards}")
                wallet = wallet + bet + bet
                break
    print(f"\nFunds: {wallet}")
    again = input("type 'yes' to play again: ")
    again = again.lower()
    if wallet >= 100:
        print("You made a 100! You win!")
    elif again == 'yes' and wallet > 0:
        play_game()
    elif wallet <= 0:
        print("You are broke. Game Over")


play_game()
