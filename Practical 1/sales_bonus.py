"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
GOOD_RAISE = 0.15
NORMAL_RAISE = 0.1
LOWER_LIMIT = 0
RAISE_BENCHMARK = 1000

sale = int(input("Please tell your salary: "))
while sale >= LOWER_LIMIT:
    if sale >= RAISE_BENCHMARK:
        bonus = sale * GOOD_RAISE
    else:
        bonus = sale * NORMAL_RAISE
    print(f'Your bonus: {bonus}$')
    sale = float(input("Please tell your salary: "))
