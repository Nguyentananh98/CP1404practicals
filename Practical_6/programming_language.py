"""
Practical 6
NGUYEN TAN ANH

estimate time: 10
completion time: 8
"""


class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection=bool, year=""):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing.lower() == "static":
            return False
        else:
            return True

    def __str__(self):
        return f'{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}'
