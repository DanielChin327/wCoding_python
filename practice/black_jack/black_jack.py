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
        except:
            print("invalid input. Write a number")
        if amount <= wallet:
            wallet = wallet - amount
            bet = amount
            print(f"Wallet: {wallet} \n Bet Amount: {bet}")
            return bet
        elif amount > wallet:
            print("Insufficent funds...")



def user_hand():
    while True:
        user_hand = deal_hand()
        print(f"Your hand is {user_hand}")
        convert_card_value(user_hand)
        total = sum(convert_card_value)
        if total > 21:
            "Bust! You Lose!"
            break
        else:
            draw = print("draw again? (y/n)")


user_hand()
user_hand()
user_hand()
user_hand()
user_hand()
