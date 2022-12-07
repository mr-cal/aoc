from collections import deque

with open("./input.txt") as file:
    data = file.read().strip()

word: deque = deque(data[0:3])

for index, byte in enumerate(data[3:]):
    word.append(byte)

    if sorted(list(word)) == sorted(list(set(list(word)))):
        print(f"first 4 unique bytes found at index = {index+4}")
        break

    word.popleft()


word = deque(data[0:13])

for index, byte in enumerate(data[13:]):
    word.append(byte)

    if sorted(list(word)) == sorted(list(set(list(word)))):
        print(f"first 14 unique bytes found at index = {index+14}")
        break

    word.popleft()
