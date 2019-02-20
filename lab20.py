"""
Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

Convert the input string into a list of ints
Slice off the last digit. That is the check digit.
Reverse the digits.
Double every other element in the reversed list.
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid.
"""


def checkCard(cardString):
    cardIntList = [int(i) for i in cardString]
    checkDigit = cardIntList.pop()
    reversedCardIntList = list(reversed(cardIntList))
    cardSum = 0
    counter = 1
    for i in range(len(reversedCardIntList)):
        if counter % 2 == 1:
            doubledValue = reversedCardIntList[i]*2
            if doubledValue > 9:
                cardSum += doubledValue - 9
            else:
                cardSum += doubledValue
        else:
            cardSum += reversedCardIntList[i]
        counter += 1

    cardCheckSum = int(str(cardSum)[-1])

    if cardCheckSum == checkDigit:
        return "Valid."
    else:
        return "Invalid."


def main():
    inputCard = input("Enter the 16-digit card number: ")
    print(f"Card is {checkCard(inputCard)}")


if __name__ == '__main__':
    main()
