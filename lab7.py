"""
#Random Password Generator -- Advanced V2
#Josh Easley
#Let's generate a password ten characters long using a loop (while loop or for loop)
#and random.choice, this will be a string of random characters.
#ASCII alphanumeric range 33-122

Allow the user to choose how many characters the password will be.

Advanced Version 2
Allow the user to choose how many letters, numbers, and punctuation characters they want in their password. Mix everything up using list(), random.shuffle(), and ''.join().
"""
import random

punctuation_list = [33,34,39,44,46,58,59,63,96]
letters_list = []

passwordString = ""

passwordLength = int(input("How many characters long would you like your password to be?: "))
numLetters = int(input("How many letters would you like in your password?: "))
numNumbers = int(input("How many numbers would you like in your password?: "))
numPunctuation = int(input("How many punctuation characters would you like in your password?: "))

for x in range(passwordLength):

    if numNumbers > 0:
        for i in range(0,numNumbers):
            passwordString += chr(random.randint(48,57))

    if numLetters > 0:
        for i in range(65,90):
            letters_list.append(chr(i))

        for x in range(97,122):
            letters_list.append(chr(x))

        for y in range(0,numLetters-1):
            passwordString += letters_list[random.randint(0,len(letters_list)-1)]

    if numPunctuation > 0:
        for i in range(0,numLetters-1):
            passwordString += chr(punctuation_list[random.randint(0,len(punctuation_list)-1)])

print(passwordString)
