import operator

lines = open('input.txt').readlines()
letter_column_map = [dict() for x in range(len(lines[0].strip()))]
for lline in lines:
    line = lline.strip()
    for col in range(len(line)):
        if line[col] in letter_column_map[col]:
            letter_column_map[col][line[col]] += 1
        else:
            letter_column_map[col][line[col]] = 1
message_part1 = ''
message_part2 = ''
for col in letter_column_map:
    scol = sorted(col.items(), key=operator.itemgetter(1), reverse=True)
    message_part1 += scol[0][0]
    message_part2 += scol[-1][0]
print message_part1
print message_part2
