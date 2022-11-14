"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            convert_farenheit()
        elif choice == "F":
            convert_celsius()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius():
    """convert farenheit to celsius"""
    fahrenheit = float(input("Farenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f'Result: {celsius:.2f} C')


def convert_farenheit():
    """convert celsius to farenheit"""
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")

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
