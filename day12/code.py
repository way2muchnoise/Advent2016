def cpy(registers, value, register):
    if value in registers:
        registers[register] = registers[value]
    else:
        registers[register] = int(value)


def inc(registers, register):
    registers[register] += 1


def dec(registers, register):
    registers[register] -= 1


def jnz(registers, register, jmp, current_line):
    if (register in registers and registers[register] is not 0)\
            or (register not in registers and register is not 0):
        return current_line + int(jmp)
    return None


registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
current_line = 0
lines = open('input.txt').readlines()
while current_line < len(lines):
    line = lines[current_line]
    splitted = line.strip().split(' ')
    new_line = None
    if line.startswith('cpy'):
        cpy(registers, splitted[1], splitted[2])
    elif line.startswith('inc'):
        inc(registers, splitted[1])
    elif line.startswith('dec'):
        dec(registers, splitted[1])
    elif line.startswith('jnz'):
        new_line = jnz(registers, splitted[1], splitted[2], current_line)
    if new_line:
        current_line = new_line
    else:
        current_line += 1
print registers['a']
