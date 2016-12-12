import re

compressed = open('input.txt')
uncompressed = ''
c = compressed.read(1)
while c:
    if c == '(':
        letters = compressed.read(1)
        nxt = compressed.read(1)
        while nxt != 'x':
            letters += nxt
            nxt = compressed.read(1)
        times = compressed.read(1)
        nxt = compressed.read(1)
        while nxt != ')':
            times += nxt
            nxt = compressed.read(1)
        current = compressed.read(int(letters))
        uncompressed += (current * int(times))
    else:
        uncompressed += c
    c = compressed.read(1)
print uncompressed
print len(uncompressed)
compressed.close()

pattern = re.compile(r'\((\d+)x(\d+)\)')


def recurse_decompress(string, pos=0, endpos=None):
    match = pattern.search(string[pos:endpos])
    length = 0
    while match:
        times = int(match.group(2))
        length += match.start(0)
        length += recurse_decompress(string, pos + match.end(0), pos + match.end(0) + int(match.group(1))) * times
        pos = pos + match.end(0) + int(match.group(1))
        match = pattern.search(string[pos:endpos])
    if length is 0:
        length = endpos - pos
    return length

print recurse_decompress(open('input.txt').readline().strip())
