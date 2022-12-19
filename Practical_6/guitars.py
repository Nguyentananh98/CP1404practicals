"""
Practical 6
NGUYEN TAN ANH

estimate time: 15
completion time: 20
"""

from Practical_6.guitar import Guitar


def main():
    """ create a loop to ask for guitar information and display it"""
    guitars = []
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print('My guitars!')
    name = input('Name: ')

    while name != '':
        year = int(input('Year: '))
        cost = float(input('Cost: '))

        guitars.append(Guitar(name, year, cost))
        print(Guitar(name, year, cost))

        print('My guitars!')
        name = input('Name: ')

    print('Name: ')
    print()
    print('...snip...')
    print()

    guitars.sort()

    for i, guitar in enumerate(guitars):
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        else:
            vintage_string = ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
