import numpy as np


def shift_col(matrix, col, amount):
    while amount > 0:
        last = matrix[-1][col]
        for row in reversed(range(len(matrix)-1)):
            matrix[row+1][col] = matrix[row][col]
        matrix[0][col] = last
        amount -= 1


def shift_row(matrix, row, amount):
    matrix[row] = np.roll(matrix[row], amount)


matrix = np.zeros((6, 50), dtype=int)
lines = open('input.txt').readlines()
for line in lines:
    if line.startswith('rect'):
        x_size = int(line.split('x')[0].split(' ')[-1])
        y_size = int(line.split('x')[1])
        for x in range(x_size):
            for y in range(y_size):
                matrix[y][x] = 1
    elif line.startswith('rotate'):
        axis = line.split(' ')[2][0]
        index = line.split(' ')[2].split('=')[-1]
        amount = line.split(' ')[-1].strip()
        if axis is 'y':
            shift_row(matrix, int(index), int(amount))
        elif axis is 'x':
            shift_col(matrix, int(index), int(amount))
for y in range(len(matrix)):
    line = ''
    for x in range(len(matrix[y])):
        if matrix[y][x] == 1:
            line += '#'
        else:
            line += ' '
        if x % 5 is 0:
            line += ' '
    print line
print
print np.count_nonzero(matrix)
