from collections import deque
from copy import deepcopy

instructions = []

# find number of stacks
max_stacks: int = 0
with open("./input.txt") as file:
    for line in file:
        # parse crate stacks
        if line.strip().startswith("["):
            max_stacks = max(max_stacks, len(line) // 4)


stacks = [deque() for i in range(max_stacks)]

with open("./input.txt") as file:
    for line in file:
        # parse crate stacks
        if line.strip().startswith("["):
            for index, char in enumerate(line):
                if index % 4 == 1 and char != ' ':
                    stack_number = (index - 1) // 4
                    stacks[stack_number].appendleft(char)

        # parse instructions
        elif line.startswith("move"):
            _, quantity, _, start, _, end = line.strip().split(" ")
            instructions.append(tuple([quantity, start, end]))

super_stacks = deepcopy(stacks)

# cratemover 9000
for instr in instructions:
    quantity = int(instr[0])
    start = int(instr[1])
    end = int(instr[2])
    for _ in range(quantity):
        stacks[end-1].append(stacks[start-1].pop())

first_output = ""
for stack in stacks:
    first_output += stack.pop()

# cratemover 9001
for instr in instructions:
    quantity = int(instr[0])
    start = int(instr[1])
    end = int(instr[2])

    # I am too lazy to convert the deques to another data structure,
    # so let's play Towers of Hanoi with deques
    temp = deque()
    for i in range(quantity):
        temp.append(super_stacks[start-1].pop())
    for _ in range(len(temp)):
        super_stacks[end-1].append(temp.pop())

second_output = ""
for stack in super_stacks:
    second_output += stack.pop()

print(f"cratemover 9000: {first_output}")
print(f"cratemover 9001: {second_output}")
