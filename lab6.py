
"""
Rock Paper Scissors Simulator -- Advanced V2
Josh Easley
#The computer will ask the user for their choice (rock, paper, scissors)
#The computer will randomly choose rock, paper or scissors
#Determine who won and tell the user
#Let's list all the cases:

#rock vs rock (tie)
#rock vs paper
#rock vs scissors
#paper vs rock
#paper vs paper
#paper vs scissors
#scissors vs rock
#scissors vs paper
#scissors vs scissors
"""
import random

choice = continuePlayingInput = computerChoice = ""

#Result dictionary. Keys - objects choices. Values - wins against, loses against, ties against.
#Usage: resultsDict[your choice][opponent's choice]
resultsDict = {'rock':{'scissors':'win','rock':'tied','paper':'lose'},'paper':{'scissors':'lose','rock':'win','paper':'tied'},'scissors':{'scissors':'tie','rock':'lose','paper':'win'}}

while True:
    choice = input("What is your choice [rock/paper/scissors]? ")
    if choice in list(resultsDict.keys()):
        computerChoice = random.choice(list(resultsDict.keys()))
        print('The computer chose ' + computerChoice)

        print("You " + resultsDict[choice][computerChoice] + ".")
        continuePlayingInput = input("Keep playing? [y/n]: ")
        if continuePlayingInput == 'y':
            computerChoice = ""
            continue
        else:
            print("Thanks for playing!")
            break
    else:
        print("Invalid input.")
