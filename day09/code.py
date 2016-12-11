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
