# Advent of Code
# Day 2
# https://adventofcode.com/2019/day/2

for line in open("input.txt"):
    input = line.split(",")

code = []
for i in input:
    code.append(int(i))

code_old = code.copy()

code[1] = 12
code[2] = 2

# Puzzle 1
i = 0
while code[i] != 99:
    if code[i] == 1:
        code[code[i+3]] = code[code[i+1]] + code[code[i+2]]
    if code[i] == 2:
        code[code[i+3]] = code[code[i+1]] * code[code[i+2]]
    i += 4
print("First Puzzle:", code[0])


# Puzzle 2
def computer(opcode):
    i = 0
    while opcode[i] != 99:
        if opcode[i] == 1:
            opcode[opcode[i+3]] = opcode[opcode[i+1]] + opcode[opcode[i+2]]
        if opcode[i] == 2:
            opcode[opcode[i+3]] = opcode[opcode[i+1]] * opcode[opcode[i+2]]
        i += 4
    return opcode[0]

for i in range(0, 100):
    for j in range(0, 100):
        code = code_old.copy()
        code[1] = i
        code[2] = j

        ret = computer(code)

        if ret == 19690720:
            noun = i
            verb = j
            break

print("Second Puzzle: noun:", noun, "verb:", verb, "Answer:", (100 * noun + verb))
