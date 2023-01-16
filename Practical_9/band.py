""""
CP1404 -NGUYEN TAN ANH
JC950881
PRACTICAL 9
"""


class Band:
    def __init__(self, name=""):
        self.name = name
        self.musicians = []

    def add(self, musician):
        """add the musician to the band"""
        self.musicians.append(musician)

    def __str__(self):
        """display band with musician and instruments"""
        musician_string = ""
        for number, musician in enumerate(self.musicians):
            guitars = ""
            for number_count, guitar in enumerate(musician.instruments):
                guitar_information = guitar.__str__()
                guitars += guitar_information
                if number_count < len(musician.instruments) - 1:
                    guitars += ", "
            musician_string += f'{musician.name} ([{guitars}])'
            if number < len(self.musicians) - 1:
                musician_string += ", "
        return f'{self.name} ([{musician_string}])'

    def play(self):
        """play the instrument of musician in the band"""
        for musician in self.musicians:
            print(musician.play())
