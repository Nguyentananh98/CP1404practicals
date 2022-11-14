for i in range(1, 21, 2):
    print(i, end=' ')
print()

"""a"""
for i in range(0, 101, 10):
    print(i, end=' ')


"""""b"""
for i in range(20, 0, -1):
    print(i, end=' ')


"""c"""
number_star = int(input('Number of stars: '))
for i in range(0, number_star):
    print('*', end='')

"""d"""
number_star = int(input('Number of stars: '))
for line in range(0, number_star):
    for star in range(0, line + 1):
        print('*', end='')
    print()
