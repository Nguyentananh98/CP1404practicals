"""
Practical 06
NGUYEN TAN ANH
"""
CURRENT_YEAR = 2022
VINTAGE_CUTOFF = 50


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """
        Initiate the variable for the guitar object
        :param name: string of the name
        :param year: int, year of creation
        :param cost: float, price of the guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """return the information of the guitar"""
        return f'{self.name} ({self.year}) : ${self.cost}'

    def get_age(self):
        """get the age of the guitar to the current year"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """check if the guitar is vintage"""
        if self.get_age() >= VINTAGE_CUTOFF:
            return True
        else:
            return False

    def __lt__(self, other):
        """return the attribute to be compare when sort"""
        return self.year < other.year
