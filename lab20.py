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
# testCard = '4563670208287350'
testCard = '4556737586899855'
print(len(testCard))
# inputCard = input("Enter the 16-digit card number: ")
inputCard = testCard


def checkCard(cardString):
    cardIntList = [int(i) for i in cardString]
    checkDigit = cardIntList.pop()
    # print(checkDigit)
    # print(len(cardIntList))
    reversedCardIntList = list(reversed(cardIntList))
    # print(len(reversedCardIntList))
    cardSumList = []
    # oddItems = reversedCardIntList[1::2]

    for i in range(len(reversedCardIntList)):
        if i % 2 == 1:
            # print(i)
            doubledValue = reversedCardIntList[i]*2
            print(doubledValue)
            cardSumList.append(doubledValue) if doubledValue < 10 else cardSumList.append(doubledValue - 9)
        else:
            cardSumList.append(reversedCardIntList[i])

    print(sum(cardSumList))
    """
    if str(cardSumList)[1] == checkDigit:
        return "Valid."
    else:
        return "Invalid."
    """

print(checkCard(inputCard))

#print(cardIntList)
