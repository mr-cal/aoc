subset_count: int = 0
intersection_count: int = 0

with open("./input.txt") as file:
    for index, line in enumerate(file):
        left_begin, left_end = line.strip().split(",")[0].split("-")
        right_begin, right_end = line.strip().split(",")[1].split("-")
        left_set = set(range(int(left_begin), int(left_end)+1))
        right_set = set(range(int(right_begin), int(right_end)+1))

        if left_set.issubset(right_set) or right_set.issubset(left_set):
            subset_count += 1

        if len(left_set.intersection(right_set)):
            intersection_count += 1

print(f"{subset_count=}")
print(f"{intersection_count=}")
