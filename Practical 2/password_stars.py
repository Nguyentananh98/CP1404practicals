"""
CP1404
NGUYEN TAN ANH -JC950881
Practical_2


pseudocode

function main()
    password = get_password(8)
    display_asterisk(password)


function display_asterisk(password)
    for i from 1 to length of password
        display '*'


function get_password(minimum_length)
    get password
    while length of password < minimum_length
        display password length has to be more than 8 message
        get password
    return password


main()

code
"""

MINIMUM_LENGTH = 8


def main():
    """get password and display stars of password length"""
    password = get_password(MINIMUM_LENGTH)
    display_asterisk(password)


def display_asterisk(password):
    """display asterisk that have the length of the password"""
    for i in range(len(password)):
        print('*', end='')


def get_password(minimum_length):
    """check if the password have minimum required length"""
    password = input("Please enter your password: ")
    while len(password) < minimum_length:
        print("THe password length must be 8 letters or more!")
        password = input("Please enter your password: ")
    return password


main()
