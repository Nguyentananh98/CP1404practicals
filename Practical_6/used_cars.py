"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.

estimate time: 5
completion time: 16
"""

from Practical_6.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(fuel=180, name='Car')
    print(my_car.name)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    limo = Car(100, name='Limo')
    limo.add_fuel(20)
    print(limo.fuel)
    print(limo.name)
    limo.drive(115)

    print(my_car)
    print(limo)


main()


