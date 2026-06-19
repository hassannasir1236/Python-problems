import random

cards = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11
}

# Use lists instead of dictionaries
computer_cards = []
user_cards = []


def computerTurn():
    card = random.choice(list(cards.keys()))
    computer_cards.append(card)

    total = 0
    for card in computer_cards:
        total += cards[card]

    return total


def userTurn():
    card = random.choice(list(cards.keys()))
    user_cards.append(card)

    total = 0
    for card in user_cards:
        total += cards[card]

    return total


def calculate():
    # Give two cards to each player
    computerTurn()
    computerTurn()

    userTurn()
    userTurn()

    print("Computer first card:", computer_cards[0])
    print("Your cards:", user_cards)
    print("Your score:", sum(cards[card] for card in user_cards))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":

    computer_cards.clear()
    user_cards.clear()

    calculate()