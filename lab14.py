"""
Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).

a ticket costs $2
if 1 number matches, you win $4
if 2 numbers match, you win $7
if 3 numbers match, you win $100
if 4 numbers match, you win $50,000
if 5 numbers match, you win $1,000,000
if 6 numbers match, you win $25,000,000
One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets. Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.

Steps

Generate a list of 6 random numbers representing the winning tickets
Start your balance at 0
Loop 100,000 times, for each loop:
Generate a list of 6 random numbers representing the ticket
Subtract 2 from your balance (you bought a ticket)
Find how many numbers match
Add to your balance the winnings from your matches
After the loop, print the final balance
Version 2

The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses.
"""
import random


def buyTickets(numTickets, payout_dict):
    balance = expenses = 0
    for i in range(numTickets):
        balance -= 2  # Buy a ticket.
        expenses += 2  # Add the cost of a ticket to expenses.
        matchCounter = 0
        winning_numbers = [random.randint(1, 99) for i in range(0, 6)]
        pick_numbers = [random.randint(1, 99) for i in range(0, 6)]
        for i in range(len(pick_numbers)):
            if pick_numbers[i] == winning_numbers[i]:
                matchCounter += 1
        balance += payout_dict[matchCounter]

        print(f"Your final balance is: ${balance}")
        print(f"You spent {expenses} for a total ROI of {balance-expenses}")


def calculate_odds(numMatches, payout_dict):
    """
    numMatches = what number of winning numbers you want
    to calculate the odds for.
    """
    winning_numbers = [random.randint(1, 99) for i in range(0, 6)]
    tickets = 0
    hasWonYet = False
    while hasWonYet is False:
        tickets += 1
        pick_numbers = [random.randint(1, 99) for i in range(0, 6)]
        matchCounter = 0
        for i in range(len(pick_numbers)):
            if pick_numbers[i] == winning_numbers[i]:
                matchCounter += 1
        if matchCounter >= numMatches:
            hasWonYet = True
    print(f"You bought {tickets} tickets to win {payout_dict[numMatches]}")


def main():
    payout_dict = {
        0: 0,
        1: 4,
        2: 7,
        3: 100,
        4: 50000,
        5: 1000000,
        6: 25000000
    }
    calculate_odds(6, payout_dict)


if __name__ == '__main__':
    main()
