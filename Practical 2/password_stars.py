"""
CP1404
NGUYEN TAN ANH -JC950881
Practical_2
"""

MINIMUM_LENGTH = 8


def main():
    password = get_password()
    display_asterisk(password)


def display_asterisk(password):
    """display asterisk that have the length of the password"""
    for i in range(len(password)):
        print('*', end='')


def get_password():
    """check if the password have minimum required length"""
    password = input("Please enter your password: ")
    while len(password) < MINIMUM_LENGTH:
        print("THe password length must be 8 letters or more!")
        password = input("Please enter your password: ")
    return password


main()
