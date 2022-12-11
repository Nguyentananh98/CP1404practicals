"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()

while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

# write a loop to print all code and states neatly lined
max_code = max([len(abbrieviation) for abbrieviation in CODE_TO_NAME.keys()])
max_name = max([len(state_name) for state_name in CODE_TO_NAME.values()])

for code in CODE_TO_NAME.keys():
    print(f'{code:{max_code}} is {CODE_TO_NAME[code]:{max_name}}')

# using EAFP approach
state_code = input("Enter short state: ").upper()

while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
