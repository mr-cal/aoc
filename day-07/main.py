from collections import deque

steps: deque = deque()

current_step: dict = {}

with open("./input2.txt", encoding="utf8") as file:
    for line in file:
        line = line.strip()
        print(f"parsing {line=}")
        # if line is a command, append the previous step to the queue and start a new step
        if line.startswith("$"):
            if len(current_step):
                steps.append(current_step)
            current_step={"command": line, "output": []}

        # otherwise parse the output from the command
        else:
            current_step["output"].append(line)



for _ in range(len(steps)):
    print(steps.popleft())


# pass dictionary around, probably?
def recurse_directories(depth: int = 0) -> dict:
    dir_tree = {}
    if len(steps):
        step = steps.popleft()
        if step["command"] == "cd /":
            pass
        elif step["command"] == "ls":
            # fill in the current directory contents
            pass
        elif step["command"] == "cd ..":
            # return up a directory
            return dir_tree
        else:
            # cd into a directory
            recurse_directories(depth=depth+1)
    else:
        return dir_tree


directory = recurse_directories(depth=0)
print(directory)

# I don't enjoy tree traversal and recursion, I'm giving up on day 7
