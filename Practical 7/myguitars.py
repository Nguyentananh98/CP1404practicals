"""
Programming 2
NGUYEN TAN ANH - JC950881
PRACTICAL 7
"""
from guitar import Guitar


def main():
    in_file = open('guitars.csv', 'r')
    content = in_file.readlines()

    guitars = []
    for line in content:
        line = line.strip().split(',')
        guitar = Guitar(line[0], line[1], line[2])
        guitar = guitars.append(guitar)

    guitars.sort()

    for item in guitars:
        print(item)


main()

