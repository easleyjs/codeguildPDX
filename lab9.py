#Two words are anagrams of each other if the letters of one can be rearranged to fit the other. e.g. anagram and nag a ram.

#Write another function check_anagram that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not. The procedure for comparing the two strings is as follow:

#Convert each word to lower case (lower)
#Remove all the spaces from each word (replace)
#Sort the letters of each word (sorted)
#Check if the two are equal

phraseOne = input('Enter the first phrase: ')
phraseTwo = input('Enter the second phrase: ')

phraseOne = sorted(phraseOne.replace(" ","").lower())
phraseTwo = sorted(phraseTwo.replace(" ","").lower())

if phraseOne == phraseTwo:
    print('The phrases match.')
else:
    print('The phrases do not match')
