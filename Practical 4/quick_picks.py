"""
Practical 04 - quick picks
Nguyen Tan Anh - JC950881
"""
import random

quick_pick = int(input('How many quick picks? '))

for line in range(quick_pick):
    number_line = []
    while len(number_line) < 6:
        random_number = random.randint(1, 45)
        if random_number not in number_line:
            number_line.append(random_number)
    for number in number_line:
        print(f'{number:2}', end=' ')
    print()
