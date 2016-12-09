import copy


def change_dir(c, current_dir):
    if c is 'L':
        current_dir -= 1
    elif c is 'R':
        current_dir += 1
    if current_dir > 3:
        current_dir = 0
    elif current_dir < 0:
        current_dir = 3
    return current_dir


def move_steps(distance, position, positions, HQ_pos):
    for i in range(0, distance):
        new_position = position(i)
        if HQ_pos[0] is None and new_position in positions:
            HQ_pos[0] = new_position[0]
            HQ_pos[1] = new_position[1]
        positions.append(new_position)


def move(current_dir, distance, position, positions, HQ_pos):
    if current_dir is 0:
        move_steps(distance, lambda i: [position[0]+i+1, position[1]], positions, HQ_pos)
        position[0] += distance
    elif current_dir is 1:
        move_steps(distance, lambda i: [position[0], position[1] + i + 1], positions, HQ_pos)
        position[1] += distance
    elif current_dir is 2:
        move_steps(distance, lambda i: [position[0] - i - 1, position[1]], positions, HQ_pos)
        position[0] -= distance
    elif current_dir is 3:
        move_steps(distance, lambda i: [position[0], position[1] - i - 1], positions, HQ_pos)
        position[1] -= distance
    return position


# dir can be 0 -> 3
current_dir = 0
HQ_pos = [None, None]
position = [0, 0]
positions = list()
steps = open('input.txt').readline().split(', ')
for step in steps:
    current_dir = change_dir(step[0], current_dir)
    move(current_dir, int(step[1:]), position, positions, HQ_pos)
print 'Part1: HQ location: ' + repr(position) + ' total distance: ' + repr(abs(position[0]) + abs(position[1]))
print 'Part2: HQ location: ' + repr(HQ_pos) + ' total distance: ' + repr(abs(HQ_pos[0]) + abs(HQ_pos[1]))
