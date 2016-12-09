import hashlib

door_id = open('input.txt').readline()
n = 0
password_part1 = ''
password_part2 = [''] * 8
hex_hash = hashlib.md5(door_id+repr(n)).hexdigest()
while len(password_part1) < 8 or '' in password_part2:
    while hex_hash[:5] != '00000':
        n += 1
        hex_hash = hashlib.md5(door_id + repr(n)).hexdigest()
    print hex_hash
    if len(password_part1) < 8:
        password_part1 += hex_hash[5]
    if hex_hash[5].isdigit() and int(hex_hash[5]) < 8 and password_part2[int(hex_hash[5])] is '' and '' in password_part2:
        password_part2[int(hex_hash[5])] = hex_hash[6]
    n += 1
    hex_hash = hashlib.md5(door_id + repr(n)).hexdigest()
print password_part1
print ''.join(password_part2)
