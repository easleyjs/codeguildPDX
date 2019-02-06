#lab11.py
"""
> What is the operation you'd like to perform? +
> What is the first number? 5
> What is the second number? 12
> 5 + 12 = 17

Version 2

Allow the user to keep performing operations until they say 'done'. Use while True and break. Below is some sample input/output.

> what is the operation you'd like to perform? +
> what is the first number? 5
> what is the second number? 12
> 5 + 12 = 17
> what is the operation you'd like to perform? done
> goodbye!
"""
def calculate(operator,firstNumber,secondNumber):
    switchDict = {
        '+': firstNumber+secondNumber,
        '-': firstNumber-secondNumber,
        '*': firstNumber*secondNumber,
        '/': firstNumber/secondNumber,
        '%': firstNumber%secondNumber
    }
    return switchDict.get(operator)

continueCalculating = True
while continueCalculating is True:
    operation = input("What operation would you like to perform? [+ - * / %] or enter 'done' to end: ")
    if operation == 'done':
        continueCalculating = False
        break
    else:
        firstNumber = float(input("What is the first number?: "))
        secondNumber = float(input("What is the second number?: "))
        print(f"Result {calculate(operation,firstNumber,secondNumber)}")
