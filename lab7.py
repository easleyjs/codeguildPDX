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
from random import randint

def getLetterList():
    return [chr(x) for x in (list(range(65,91)) + list(range(97,123)))]

def getNumberList():
    return [chr(x) for x in range(48,57)]

def getPunctuationList():
    static_punctuation_list = [33,34,39,44,46,58,59,63,96]
    return [chr(x) for x in static_punctuation_list]

def getRandomCharacters(charType,numChars):
    if charType == 'letter':
        source_list = getLetterList()
    elif charType == 'number':
        source_list = getNumberList()
    elif charType == 'punctuation':
        source_list = getPunctuationList()
    return "".join([source_list[randint(0,len(source_list)-1)] for x in range(0,numChars)])

passwordString = ""
passwordLength = int(input("How many characters long would you like your password to be?: "))
numLetters = int(input("How many letters would you like in your password?: "))
numNumbers = int(input("How many numbers would you like in your password?: "))
numPunctuation = int(input("How many punctuation characters would you like in your password?: "))

if numNumbers > 0:
    passwordString += getRandomCharacters('number',numNumbers)
if numLetters > 0:
    passwordString += getRandomCharacters('letter',numLetters)
if numPunctuation > 0:
    passwordString += getRandomCharacters('punctuation',numPunctuation)

print("Your password is: " + passwordString)
