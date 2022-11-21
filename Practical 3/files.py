"""
CP1404 -Practical 3
NGUYEN TAN ANH
JC950881
"""

# question 1

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
