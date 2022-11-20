"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion

function main()
    display menu
    get choice in uppercase
    while choice != "Q"
        if choice == "C"
            convert_farenheit()
        else if choice == "F"
            convert_celsius()
        else
            print("Invalid option")
        display menu
        get choice in uppercase
    display thank message


function convert_celsius()
    get farenheit
    celsius = 5 / 9 * (fahrenheit - 32)
    display celcius in 2 float number


function convert_farenheit()
    get celcius
    fahrenheit = celsius * 9.0 / 5 + 32
    display celcius in 2 float number


main()
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """covert celcius to farenheit and farenheit to celcius"""
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


main()
