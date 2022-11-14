"""
pseudocode

get number of item
while num_item < 0
    display invalid message
    get number of item

sum_price = 0
for i from 0 to num_item
    get item_price with i+1
    add item_price to sum_price

if sum_price > 100
    sum_price = sum_price * (1-DISCOUNT)
display sum_price

code
"""
DISCOUNT = 0.1  # discount 10% if total price over 100$
DISCOUNT_PRICE = 100  # apply discount if total price greater than this level
LOWER_LIMIT = 0

sum_price = 0

number_item = int(input('Number of items: '))
while number_item < LOWER_LIMIT:
    print("Invalid number of items!")
    number_item = int(input('Number of items: '))

for i in range(number_item):
    item_price = float(input(f'Price of item {i+1}: '))
    sum_price += item_price

if sum_price > DISCOUNT_PRICE:
    sum_price *= (1-DISCOUNT)

print(f'Total price for 3 items is ${sum_price:.2f}')
