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
# import math
one_to_teens_dict = {
                1: 'one',
                2: 'two',
                3: 'three',
                4: 'four',
                5: 'five',
                6: 'six',
                7: 'seven',
                8: 'eight',
                9: 'nine',
                10: 'ten',
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


def num_to_words(inputNumber):
    hundredsValue = tensAndOnes = tensValue = onesValue = 0
    numWords = ""
    tensAndOnes = inputNumber % 100
    if inputNumber == 0:
        return "zero"
    if inputNumber > 99:
        hundredsValue = inputNumber//100
        numWords += one_to_teens_dict[hundredsValue] + " hundred "
    if 0 < tensAndOnes < 20:
        numWords += one_to_teens_dict[tensAndOnes]
    if 20 <= tensAndOnes <= 99:
        tensValue = tensAndOnes // 10
        onesValue = inputNumber % 10
        numWords += tens_dict[tensValue] + (" " + one_to_teens_dict[onesValue] if onesValue > 0 else '')
    return numWords


def main():
    inputNumber = input("Enter a number between 0-999: ")
    print(num_to_words(inputNumber))


if __name__ == 'main':
    main()
