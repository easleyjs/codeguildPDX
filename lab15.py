"""
Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.

x = 67
tens_digit = x//10
ones_digit = x%10
Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.

Version 2

Handle numbers from 100-999.

Version 3 (optional)

Convert a number to roman numerals.

Version 4 (optional)

Convert a time given in hours and minutes to a phrase.
"""
import math
singles_dict = {
                1: 'one',
                2: 'two',
                3: 'three',
                4: 'four',
                5: 'five',
                6: 'six',
                7: 'seven',
                8: 'eight',
                9: 'nine'
}

tens_dict = {
                1: 'ten',
                2: 'twenty',
                3: 'thirty',
                4: 'forty',
                5: 'fifty',
                6: 'sixty',
                7: 'seventy',
                8: 'eighty',
                9: 'ninety'
}

double_digit_dict = {
                11: 'eleven',
                12: 'twelve',
                13: 'thirteen',
                14: 'fourteen',
                15: 'fifteen',
                16: 'sixteen',
                17: 'seventeen',
                18: 'eighteen',
                19: 'nineteen'
}


def number_to_word(inputNumber):
    numberString = onesWord = hundredsWord = ""
    divHundred = inputNumber / 100
    modHundred = inputNumber % 100
    if inputNumber % 100 >= 10:
        onesWord = double_digit_dict.get((modHundred), tens_dict.get(modHundred / 10, ''))
    else:
        onesWord = singles_dict.get(modHundred, '')

    if divHundred > 0:
        hundredsWord = singles_dict.get(divHundred, '') + " hundred "

    return hundredsWord + onesWord


print(number_to_word(960))
print(number_to_word(900))
print(number_to_word(999))
print(number_to_word(911))
print(number_to_word(9))
