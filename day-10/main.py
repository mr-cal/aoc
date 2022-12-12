from collections import namedtuple

Instruction = namedtuple("Instruction", ["command", "value", "cycles"])

instructions = []
with open("./input.txt", encoding="utf8") as file:
    for line in file:
        line = line.strip()
        if "noop" in line:
            instructions.append(Instruction("noop", 0, 1))
        else:
            command, value = line.split(" ")
            instructions.append(Instruction("addx", int(value), 2))



cycles = [1]

for instruction in instructions:
    print(instruction)
    if instruction.command == "noop":
        cycles.append(cycles[-1])
    else:
        cycles.append(cycles[-1])
        cycles.append(cycles[-1] + instruction.value)



for cycle, register in enumerate(cycles):
    print(f"{cycle=}, {register=}")

print(cycles[20])
print(cycles[60])
print(cycles[100])
print(cycles[140])
print(cycles[180])
print(cycles[220])

print(
    20 * cycles[19] +
    60 * cycles[59] +
    100 * cycles[99] +
    140 * cycles[139] +
    180 * cycles[179] +
    220 * cycles[219]
)
