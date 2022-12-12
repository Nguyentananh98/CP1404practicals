"""
Practical 6
NGUYEN TAN ANH

estimate time: 10
completion time: 8
"""


class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection=bool, year=""):
        """
        Initiate the params for the programming language objects
        :param name:
        :param typing:
        :param reflection:
        :param year:
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """ check if the language is dynamic or not"""
        if self.typing.lower() == "static":
            return False
        else:
            return True

    def __str__(self):
        """ display the information of the language"""
        return f'{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}'
