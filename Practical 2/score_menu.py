"""
CP 1404 - Practical 2
NGUYEN TAN ANH - JC950881
"""

UPPER_LEVEL = 90
MIDDLE_LEVEL = 50
UPPER_LIMIT = 100
LOWER_LIMIT = 0

MENU = """
MENU
(G)et a valid score
(P)rint result
(S)how stars 
(Q)uit
"""


def main():
    """display menu and ask user for choice, then do the task of that choice"""
    score = get_valid_score()
    print(MENU)
    choice = input("Your choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = define_result(score)
            print(f'Your score is {result}')
        elif choice == "S":
            display_asterisk(score)
        else:
            print("Invalid choice")
        choice = input("Your choice: ").upper()
    print("Farewell")


def get_valid_score():
    """get score from 0 to 100 inclusive"""
    input_score = float(input("Please enter input_score from 0-100 inclusive: "))
    while input_score < 0 or input_score > 100:
        print("Invalid input_score")
        input_score = float(input("Please enter input_score from 0-100 inclusive: "))
    return input_score


def display_asterisk(score):
    """display row of asterisk with length of score number"""
    for i in range(int(score)):
        print('*', end='')
    print()


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
