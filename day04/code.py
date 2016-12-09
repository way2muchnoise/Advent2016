import re


def compare(x, y):
    rval = cmp(y[1], x[1])
    return cmp(x[0], y[0]) if rval is 0 else rval

lines = open('input.txt').readlines()
sector_sum = 0
for line in lines:
    parts = line.split('-')
    letters = ''.join(parts[:-1])
    count = int(parts[-1].split('[')[0])
    check_sum = re.split('[\[\]]', parts[-1])[-2]
    letter_count = {}
    for letter in letters:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    letters = letter_count.keys()
    letter_count = sorted(letter_count.items(), cmp=compare)
    valid = True
    for i in range(0, len(check_sum)):
        valid &= check_sum[i] is letter_count[i][0]
    if valid:
        sector_sum += count
        shifted = {}
        for i in range(0, len(letters)):
            shifted[letters[i]] = chr(((ord(letters[i]) - ord('a') + count) % 26) + ord('a'))
        sentence = list(' '.join(parts[:-1]))
        for i in range(0, len(sentence)):
            if sentence[i] in letters:
                sentence[i] = shifted[sentence[i]]
        print ''.join(sentence) + ' ' + repr(count)
print sector_sum
