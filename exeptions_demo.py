"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
-Value error occure when the user input is float but the input type is int
2. When will a ZeroDivisionError occur?
-When the user denominator input is 0, so that a number cannot devide to zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, you can change it to a while loop
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print('Cannot devide by zero')
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")