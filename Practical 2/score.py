"""
CP1404/CP5632 - Practical 2
Refactor the broken_score in practical 1
"""

# Fix this!
UPPER_LEVEL = 90
MIDDLE_LEVEL = 50
UPPER_LIMIT = 100
LOWER_LIMIT = 0


def main():
    score = float(input("Enter score: "))
    define_result(score)


def define_result(score):
    """define the result of the input score"""
    if (score < LOWER_LIMIT) and (score > UPPER_LIMIT):
        print("Invalid score")
    elif score >= UPPER_LEVEL:
        print("Excellent")
    elif score >= MIDDLE_LEVEL:
        print("Passable")
    else:
        print("Bad")


main()
