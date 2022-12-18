"""
Programming 2
Practical 6
NGUYEN TAN ANH


estimate time: 5
completion time: 5
"""

from Practical_6.guitar import Guitar


def main():
    """test the guitar class"""
    gibson = Guitar('Gibson L-5 CES', 1922, 16035.40)
    tremolo = Guitar('Tremolo', 2013, 1500)
    # test get_age()
    print(f'Gibson L-5 CES get_age() - Expected 100. Got {gibson.get_age()}')
    print(f'Tremolo get_age() - Expected 9. Got {tremolo.get_age()}')
    print(f'Gibson L-5 CES is_vintage() - Expected True. Got {gibson.is_vintage()}')
    print(f'Tremolo is_vintage() - Expected False. Got {tremolo.is_vintage()}')


main()
