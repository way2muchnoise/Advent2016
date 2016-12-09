pad = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

advanced_pad = [[0, 0, 1, 0, 0],
                [0, 2, 3, 4, 0],
                [5, 6, 7, 8, 9],
                [0, 'A', 'B', 'C', 0],
                [0, 0, 'D', 0, 0]]


def move(x, y, position):
    if x > 0 and position[1] + 1 < 5 and advanced_pad[position[0]][position[1]+1] is not 0:
        position[1] += 1
    elif x < 0 and position[1] - 1 > -1 and advanced_pad[position[0]][position[1]-1] is not 0:
        position[1] -= 1
    elif y > 0 and position[0] + 1 < 5 and advanced_pad[position[0]+1][position[1]] is not 0:
        position[0] += 1
    elif y < 0 and position[0] - 1 > -1 and advanced_pad[position[0]-1][position[1]] is not 0:
        position[0] -= 1


position = [1, 1]
lines = open('input.txt').readlines()
for line in lines:
    for c in line:
        if c is 'U':
            move(0, -1, position)
        elif c is 'R':
            move(1, 0, position)
        elif c is 'D':
            move(0, 1, position)
        elif c is 'L':
            move(-1, 0, position)
    print advanced_pad[position[0]][position[1]]
