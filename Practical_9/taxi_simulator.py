""""
CP1404 -NGUYEN TAN ANH
JC950881
PRACTICAL 9
"""
from Practical_9.SilverServiceTaxi import SilverServiceTaxi
from Practical_9.taxi import Taxi

TAXIS = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def main():
    current_taxi = None
    bill = 0
    print("Let's drive!")
    print("""q)uit, c)hoose taxi, d)rive""")
    choose = input(""">>> """).upper()
    while choose != "Q":
        if choose == "C":
            print("Taxis available:")
            display_taxi(TAXIS)
            current_taxi = check_input("Choose taxi: ", len(TAXIS) -1)
        elif choose == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = int(input("Drive how far? "))
                TAXIS[current_taxi].drive(distance)
                cost = TAXIS[current_taxi].get_fare()
                print(f'Your {TAXIS[current_taxi].name} cost you ${cost}')
                bill += cost
        else:
            print('Invalid option')

        print(f'Bill to date: ${bill}')
        print("Let's drive!")
        print("""q)uit, c)hoose taxi, d)rive""")
        choose = input(""">>> """).upper()

    print(f'Total trip cost: ${bill}')
    print('Taxis are now:')
    display_taxi(TAXIS)


def display_taxi(taxis):
    """display the taxi list"""
    for number, taxi in enumerate(taxis):
        print(f'{number} - {taxi.__str__()}')


def check_input(message, limit):
    """check for valid taxi choice"""
    choice = int(input(message))
    while choice > limit or choice < 0:
        print("Invalid taxi choice")
        choice = int(input(message))
    return choice


main()
