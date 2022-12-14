"""
CP1404/CP5632 - Practical 2
Refactor the broken_score in practical 1

pseudocode

function main()
    get score
    result = define_result(score)
    display result
    generate random float from 0 to 100
    random_result = define_result(random_score)
    display random_result


function define_result(score)
    if score < 0 or score > 100
        return "Invalid score"
    else if score >= 90
        return "Excellent"
    else if score >= 50
        return "Passable"
    else
        return "Bad"


main()

code
"""
import random

# Fix this!
UPPER_LEVEL = 90
MIDDLE_LEVEL = 50
UPPER_LIMIT = 100
LOWER_LIMIT = 0


def main():
    """ask for a score number and return the result of it"""
    score = float(input("Enter score: "))
    result = define_result(score)
    print(f'Your score is {result}')
    random_score = random.uniform(0, 100)
    random_result = define_result(random_score)
    print(f'The random score result is: {random_result}')


def define_result(score):
    """define the result of the input score"""
    if (score < LOWER_LIMIT) or (score > UPPER_LIMIT):
        return "Invalid score"
    elif score >= UPPER_LEVEL:
        return "Excellent"
    elif score >= MIDDLE_LEVEL:
        return "Passable"
    else:
        return "Bad"


main()
