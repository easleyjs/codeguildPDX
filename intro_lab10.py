#lab10.py
"""
Let's convert a dollar amount into a number of coins. The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. Always break the total into the highest coin value first, resulting in the fewest amount of coins. For this, you'll have to use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

Version 1
Have the user enter the total number in pennies, e.g. for $1.36, the user will enter 136. Then break that 136 into quarters (5), dimes (1), nickles (0) and pennies (1).

Advanced Version 1
Have the user enter a dollar amount (1.36), convert this to the total in pennies, and proceed as before. Do this with float() and round().

Advanced Version 2
Let the user add their own custom coins.
"""
import math

coins = {
            "Quarters":25,
            "Dimes":10,
            "Nickels":5,
            "Pennies":1
}

def customCoin(coinName,coinAmount,coins):
    coins[coinName] = coinAmount
    return coins

def makeChange(totalAmount,coins):
    remainderAmount = totalAmount
    coinAmount = 0
    print("Total Amount: $" + str(totalAmount/100))

    for coin in sorted(coins,reverse=True):
        coinAmount = math.floor(remainderAmount /coins[coin])
        print(coin + ": " + str(coinAmount))
        remainderAmount -= coinAmount*coins[coin]

inputAmount = float(input("Enter the total amount in pennies (i.e. 135 for $1.35): "))
makeCustomCoins = input("Would you like to input any custom coins? [y/n]: ")
if makeCustomCoins == 'y':
    continueCustomCoins = True
    while continueCustomCoins is True:
        customCoinAmount = int(input("What is the custom coins value in pennies?: "))
        customCoinName = input("What is the plural name for the coin [e.g. 'Dubloons']: ")
        coins = customCoin(customCoinName,customCoinAmount,coins)
        makeCustomCoins = input("Continue adding custom coins? [y/n]: ")
        if makeCustomCoins == 'n':
            continueCustomCoins = False
        else:
            continue
else:
    pass

#All optional custom coins should be entered. Make change and display.
makeChange(inputAmount,coins)
