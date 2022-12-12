"""
Practical 6
NGUYEN TAN ANH
"""

from Practical_6.guitar import Guitar


def main():
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
        year = int(input('Year: '))
        cost = float(input('Cost: '))


    print('Name: ')
    print()
    print('...snip...')
    print()
    for i, guitar in enumerate(guitars):
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        else:
            vintage_string = ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

main()
