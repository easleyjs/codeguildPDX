"""
Grader Advanced Version 2 by Josh Easley (easleyjs)
#Let's convert a number grade to a letter grade, using if and elif statements and comparisons.

#Have the user enter a number representing the grade (0-100)
#Convert the number grade to a letter grade
"""
import random

score = int(input('What was your score (0-100)?\n'))
rivalScore = randint(0,100)
rivalResult = ""

if score > rivalScore:
    rivalResult = "You beat your rival."
elif score < rivalScore:
    rivalResult = "Your rival beat you."
elif score == rivalScore:
    rivalResult = "You tied with your rival."

gradeModifier = ""
if score % 10 < 5:
    gradeModifier = "-"
elif score % 10 > 5:
    gradeModifier = "+"

if score >= 90:
    print('A'+gradeModifier)
    print(rivalResult)
elif score >= 80:
    print('B'+gradeModifier)
    print(rivalResult)
elif score >= 70:
    print('C'+gradeModifier)
    print(rivalResult)
elif score >= 60:
    print('D'+gradeModifier)
    print(rivalResult)
elif score < 60:
    print('F')
    print(rivalResult)
