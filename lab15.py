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
one_to_twenty_dict = {
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


def num_to_word(inputNumber):
    hundredsValue = tensValue = onesValue = 0
    numWords = ""
    if inputNumber > 99:
        numWords += one_to_twenty_dict[inputNumber//100] + " hundred "
        tensValue = inputNumber % 100
        onesValue = inputNumber % 100 % 10
        if 10 < (onesValue + 10) < 20:
            numWords = one_to_twenty_dict[onesValue + 10]
        else:
            tensValue = inputNumber % 100 // 10
            if tensValue != 0:
                numWords += one_to_twenty_dict[tensValue]
            if onesValue != 0:
                numWords += one_to_twenty_dict[onesValue]
    elif inputNumber <= 20:
        numWords += one_to_twenty_dict[inputNumber]

    """
    if 10 < (tensValue * 10 + onesValue) < 20:
        numWords += _dict[10 + onesValue]
    else:
        if tensValue > 0:
            numWords += tens_dict[tensValue]
        if onesValue > 0:
            numWords += singles_dict[onesValue]
    """
    return numWords
    # print(f"{tensValue} {onesValue}")
    # print(teens_dict[tensValue * 10 + onesValue])


# print(num_to_word(612))
print(num_to_word(13))
# num_to_word(13)
"""
for i in (range(25)):
    print(num_to_word(i))
"""
