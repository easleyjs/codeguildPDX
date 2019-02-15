"""
A palindrome is a word that's the same forwards or backwards, e.g. racecar. Another way to think of it is as a word that's equal to its own reverse.

Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not.

Two words are anagrams of eachother if the letters of one can be rearranged to fit the other. e.g. anagram and nag a ram.

Write another function check_anagram that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not. The procedure for comparing the two strings is as follow:

Convert each word to lower case (lower)
Remove all the spaces from each word (replace)
Sort the letters of each word (sorted)
Check if the two are equal
"""

def check_anagram(wordOne,wordTwo):
    """
    >>> print(check_anagram("race face","ecaf care"))
    race face and ecaf care are an anagram.
    """
    wordOneSorted = "".join(sorted(list(wordOne.lower().replace(" ", ''))))
    wordTwoSorted = "".join(sorted(list(wordTwo.lower().replace(" ", ''))))
    return f"{wordOne} and {wordTwo} are an anagram." if wordOneSorted == wordTwoSorted else f"{wordOne} and {wordTwo} are not an anagram."


def check_palindrome(word):
    """
    >>> print(check_palindrome("racecar"))
    racecar is a palindrome.
    """
    word = word.lower()
    return f"{word} is a palindrome." if word[::-1] == word else f"{word} is not a palindrome."




def main():
    pass

if __name__ == 'main':
    main()
