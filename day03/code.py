import re

lines = open('input.txt').readlines()
count = 0
line_pointer = 0
while line_pointer < len(lines):
    current_lines = list()
    current_lines.append(re.split('\D+', lines[line_pointer + 0].strip()))
    current_lines.append(re.split('\D+', lines[line_pointer + 1].strip()))
    current_lines.append(re.split('\D+', lines[line_pointer + 2].strip()))
    for col in range(0, 3):
        sides = [int(current_lines[0][col]),
                 int(current_lines[1][col]),
                 int(current_lines[2][col])]
        valid = True
        valid &= sides[0] + sides[1] > sides[2]
        valid &= sides[1] + sides[2] > sides[0]
        valid &= sides[0] + sides[2] > sides[1]
        if valid:
            count += 1
    line_pointer += 3
print count
