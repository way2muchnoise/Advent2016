def as_key(x, y):
    return repr(x) + ',' + repr(y)


def distance(coord1, coord2):
    return (coord1[0] - coord2[0]) ** 2 + (coord2[1] - coord2[1]) ** 2


def is_open(x, y, num):
    return bin(x*x + 3*x + 2*x*y + y + y*y + num).count('1') % 2 == 0


def check_surroundings(x, y, grid, num):
    open_neighbours = []
    if x-1 >= 0:
        if as_key(x-1, y) not in grid:
            grid[as_key(x-1, y)] = is_open(x-1, y, num)
        if grid[as_key(x-1, y)]:
            open_neighbours.append((x-1, y))
    if x+1 >= 0:
        if as_key(x+1, y) not in grid:
            grid[as_key(x+1, y)] = is_open(x+1, y, num)
        if grid[as_key(x+1, y)]:
            open_neighbours.append((x+1, y))
    if y-1 >= 0:
        if as_key(x, y-1) not in grid:
            grid[as_key(x, y-1)] = is_open(x, y-1, num)
        if grid[as_key(x, y-1)]:
            open_neighbours.append((x, y-1))
    if y+1 >= 0:
        if as_key(x, y+1) not in grid:
            grid[as_key(x, y+1)] = is_open(x, y+1, num)
        if grid[as_key(x, y+1)]:
            open_neighbours.append((x, y+1))
    return open_neighbours

number = int(open('input.txt').readline().strip())
current_x = 1
current_y = 1
destination_x = 31
destination_y = 39
destination = (destination_x, destination_y)
grid = {as_key(current_x, current_y): is_open(current_x, current_y, number)}
path = []
popped = []

while current_x is not destination_x or current_y is not destination_y:
    print (current_x, current_y)
    open_neighbours = check_surroundings(current_x, current_y, grid, number)
    possible_exits = filter(lambda x: popped.count(x) == 0 and path.count(x) == 0, open_neighbours)
    possible_exits = sorted(possible_exits,
                            lambda coord1, coord2: distance(coord1, destination) - distance(coord2, destination))
    if len(possible_exits) > 0:
        path.append((current_x, current_y))
        current_x = possible_exits[0][0]
        current_y = possible_exits[0][1]
    else:
        popped.append((current_x, current_y))
        last_cell = path.pop()
        current_x = last_cell[0]
        current_y = last_cell[1]
print (current_x, current_y)
print len(path)-1
