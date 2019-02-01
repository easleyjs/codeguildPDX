# Write your code here :-)
#Search the interwebs for an example Mad Lib
#Create a new file and save it as madlib.py
#Ask the user for each word you'll put in your Mad Lib
#Use string concatenation to put each word into the Mad Lib


shouldStop = False

while shouldStop not true:
    importantName = input('Name of an important person: ')
    adjectives = input('Three Gross Adjectives (comma separated): ').split(',')
    place = input('Place on Earth: ')

    print("We're looking for a few " + adjectives[0] + ", " + adjectives[1] + ", " + adjectives[2] + " " + importantName + "s " + "to join us in taking over " + place + " this winter!!")
    playAgain = input('Would you like to play again? (yes/no): ')
    if playAgain === 'yes':
        shouldStop = True
