#lab10.py
"""
##Averaging Numbers

We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list. Remember len will give you the length of a list.

The code below hows how to loop through an array, and prints the elements one at a time.

nums = [5, 0, 8, 3, 4, 1, 6]

# loop over the elements
for num in nums:
    print(num)

# loop over the indices
for i in range(len(nums)):
    print(nums[i])

Version 2
Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average. The following code demonstrates how to add an element to the end of a list.

"""
##Version 2

#nums = [1,2,3,4,5]

def sumNumbers(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

numberList = []

continueAdding = True
while continueAdding is True:
    numberList.append(int(input("Input a number: ")))
    shouldContinuePlaying = input("Do you want to continue adding numbers? [y/n]: ")
    if shouldContinuePlaying == 'n':
        continueAdding = False
    else:
        continue


numberSum = sumNumbers(numberList)

print("The average is %s" % (numberSum/len(numberList)))
