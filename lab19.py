"""

Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted"
Print out the current total point value and the advice.

What's your first card? Q
What's your second card? 2
What's your third card? 3
15 Hit

"""
cards = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'J': 10,
            'Q': 10,
            'K': 10,
            'A': 11
}

deck = []

def get_cards():
    cardOne = cardTwo = cardThree = 0
    advice = ""
    print("Enter cards as: %s" % str(" ".join([str(i) for i in cards])))
    cardOne = cards.get(input("What is the first card?: "), 0)
    cardTwo = cards.get(input("What is the second card?: "), 0)
    cardThree = cards.get(input("What is the third card?: "), 0)

    print(f"{cardOne} {cardTwo} {cardThree}")
    if cardTwo == 11:
        cardTwo = 1
    if cardThree == 11:
        cardThree = 1

    cardTotal = cardOne + cardTwo + cardThree

    if cardTotal == 21:
        advice = "Blackjack."
    elif cardTotal < 17:
        advice = "Hit."
    elif 21 > cardTotal >= 17:
        advice = "Stay."
    elif cardTotal > 21:
        advice = "Bust."

    return f"Card Total: {cardTotal}\nAdvice: {advice}"


print(get_cards())
