"""
Easley's Magic 8-Ball Advanced Version 2
"""

import random

playAgain = "yes"

print("Welcome to Easley's Magic 8-Ball.")

while playAgain == "yes":

    question = input("What is your question?:\n")

    answers = ['Outcome not likely.','Definitely','The future is hazy.','Ask again later.','Nope']

    print(random.choice(answers))

    playAgain = input("Would you like to play again (yes/no)? : ")
