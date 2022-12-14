"""
Practical 06
NGUYEN TAN ANH

estimate time: 20
completion time: 30
"""

from Practical_6.programming_language import ProgrammingLanguage


def main():
    """insert data of programming language and display it"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python.is_dynamic())
    print(python)
    languages = [python, ruby, visual_basic]

    print('The dynamically typed languages are:')
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
