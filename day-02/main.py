from abc import ABC, abstractmethod

class Shape(ABC):
    @property
    @abstractmethod
    def score(self):
        pass

    @property
    @abstractmethod
    def char(self):
        pass

    @property
    @abstractmethod
    def rank(self):
        pass

class Rock(Shape):
    score = 1
    char = "A"
    rank = 0

class Paper(Shape):
    score = 2
    char = "B"
    rank = 1

class Scissors(Shape):
    score = 3
    char = "C"
    rank = 2


hand_conversion = {"X": "A", "Y": "B", "Z": "C"}
shape_list = [Rock, Paper, Scissors]


class Hand:
    def __init__(self, elf_char, my_char):
        self.elf_shape = next(shape for shape in shape_list if shape.char == elf_char)
        self.my_shape = next(shape for shape in shape_list if shape.char == my_char)


# parse input to list of hands
with open("./input.txt") as file:
    hands = []
    for line in file:
        elf_char, my_char = line.split()
        my_char = hand_conversion[my_char]
        hands.append(Hand(elf_char=elf_char, my_char=my_char))

# check outcome of each hand for part 1
score_part_1 = 0
for hand in hands:
    # tie
    if hand.my_shape.char == hand.elf_shape.char:
        score_part_1 += hand.my_shape.score + 3
    # win
    elif ((hand.elf_shape.rank + 1) % 3) == hand.my_shape.rank:
        score_part_1 += hand.my_shape.score + 6
    # lose
    else:
        score_part_1 += hand.my_shape.score


# check outcome of each hand for part 2
score_part_2 = 0
for hand in hands:
    # lose
    if hand.my_shape.char == "A":
        losing_shape_rank = ((hand.elf_shape.rank - 1) % 3)
        losing_shape_score = next(shape.score for shape in shape_list if shape.rank == losing_shape_rank)
        score_part_2 += losing_shape_score
    # tie
    elif hand.my_shape.char == "B":
        score_part_2 += hand.elf_shape.score + 3
    # win
    else:
        winning_shape_rank = ((hand.elf_shape.rank + 1) % 3)
        winning_shape_score = next(shape.score for shape in shape_list if shape.rank == winning_shape_rank)

        score_part_2 += winning_shape_score + 6


print(f"{score_part_1=}")
print(f"{score_part_2=}")
