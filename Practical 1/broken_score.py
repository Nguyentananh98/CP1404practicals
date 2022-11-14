"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

#Fix this!
UPPER_LEVEL = 90
MIDDLE_LEVEL = 50
UPPER_LIMIT = 100
LOWER_LIMIT = 0

score = float(input("Enter score: "))
if (score < LOWER_LIMIT) and (score > UPPER_LIMIT):
    print("Invalid score")
elif score >= UPPER_LEVEL:
    print("Excellent")
elif score >= MIDDLE_LEVEL:
    print("Passable")
else:
    print("Bad")
