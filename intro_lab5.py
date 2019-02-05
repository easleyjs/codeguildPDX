"""
Easley's Emoticon Generator Advanced Version 2
"""

#Define a list of eyes
#Define a list of noses
#Define a list of mouths
#Randomly pick a set of eyes
#Randomly pick a nose
#Randomly pick a mouth
#Assemble and display the emoticon

import random

eyes = ['=',':',';','B','X','0']
noses = ['^','-','=']
mouths = [')','(',']','[','O']

eyeChoice = ""
noseChoice = ""
mouthChoice = ""

gameChoice = input("Would you like to build your emoticon, or generate a random one [build/random]: ")

if gameChoice == "build":
    print("You have " + str(len(eyes)) + " choices for eyes:\n"+",".join(eyes))
    eyeChoice = eyes[int(input("Which eyes would you like [0-" + str(len(eyes)-1) +"]: "))]
    print("You have " + str(len(noses)) + " choices for noses:\n"+",".join(noses))
    noseChoice = noses[int(input("Which nose would you like [0-" + str(len(noses)-1) +"]: "))]
    print("You have " + str(len(mouths)) + " choices for mouths:\n"+",".join(mouths))
    mouthChoice = mouths[int(input("Which mouth would you like [0-" + str(len(mouths)-1) +"]: "))]
    print("Your custom Emoticon => " + eyeChoice + noseChoice + mouthChoice)
elif gameChoice == "random":
    print(random.choice(eyes) + random.choice(noses) + random.choice(mouths))
else:
    print("Exiting Game.")
