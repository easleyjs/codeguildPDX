let coins = {
	Quarters:25,
	Dimes:10,
	Nickels:5,
	Pennies: 1
}



/*
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
*/

