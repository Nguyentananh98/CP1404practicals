"""
CP1404 -Practical 3
NGUYEN TAN ANH
JC950881
"""

question 1

OUTPUT_FILE = 'name.txt'

name = input('Please enter your name: ')
out_file = open(OUTPUT_FILE, 'w')
print(name, file=out_file)
out_file.close()

# question 2
INPUT_FILE = 'name.txt'

in_file = open(INPUT_FILE, 'r')
name = in_file.read()
print(f'Your name is {name}')

# question 3
OUTPUT_FILE = 'numbers.txt'
out_file = open(OUTPUT_FILE, 'w')
numbers = [17, 42, 400]
for number in numbers:
    print(number, file=out_file)
out_file.close()

"""open numbers.txt and read the first 2 numbers"""
INPUT_FILE = 'numbers.txt'
in_file = open(INPUT_FILE, 'r')
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
print(f'The sum of the first and second number is: {number_1 + number_2}')

# question 4
INPUT_FILE = 'numbers.txt'

in_file = open(INPUT_FILE, 'r')
line_sum = 0
for line in in_file:
    line_sum += int(line)

print(f'Total of the file numbers is: {line_sum}')


