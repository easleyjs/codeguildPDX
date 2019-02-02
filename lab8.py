#Let's play 'Guess the Number', the computer will guess a random int between 1 and 10. The user will then try to guess the number, and the program will tell them whether they're right or wrong.
#Advanced Version 1
#Using a while loop, allow the user to guess 10 times. If they fail to guess the number after 10 tries, the user is told they've lost.

import random
userChoice = ""
gameWon = False
#userChoice = input("Pick a random number 1-10: ")

computerChoice = random.randint(1,10)

counter = 0

while counter < 11:
    userChoice = int(input("Pick a number 1-10: "))
    if userChoice == computerChoice:
        print('Good job, you guessed it!')
        gameWon = True
        break
    elif userChoice < computerChoice:
        print('Your choice was lower than the number..')
    elif userChoice > computerChoice:
        print('Your choice was higher than the number..')
    counter += 1

if gameWon == False:
    print('Better luck next time!')
