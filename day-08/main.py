trees = []
count: int = 0
max_score: int = 0

# parse data as list of lists
with open("./input.txt", encoding="utf8") as file:
    for line in file:
        row = []
        for char in line.strip():
            row.append(char)
        trees.append(row)

# part 1
for row_index, row in enumerate(trees):
    for column_index, tree in enumerate(row):
        if (
            row_index == 0 or                  # left side
            row_index == len(trees)-1 or       # right side
            column_index == 0 or               # top side
            column_index == len(trees[0])-1 or # bottom side
            not [neighbor for neighbor in row[:column_index] if neighbor >= tree] or                   # walk left
            not [neighbor for neighbor in row[column_index+1:] if neighbor >= tree]or                  # walk right
            not [m_row[column_index] for m_row in trees[:row_index] if m_row[column_index] >= tree] or # walk up
            not [m_row[column_index] for m_row in trees[row_index+1:] if m_row[column_index] >= tree]  # walk down
        ):
            count += 1

# part 2
for row_index, row in enumerate(trees):
    for column_index, tree in enumerate(row):
        left_score = right_score = up_score = down_score = 0
        if row_index == 0 or row_index == len(trees)-1 or column_index == 0 or column_index == len(trees[0])-1:
            continue

        for neighbor in reversed(row[:column_index]):
            left_score += 1
            if neighbor >= tree:
                break

        for neighbor in row[column_index+1:]:
            right_score += 1
            if neighbor >= tree:
                break

        for m_row in reversed(trees[:row_index]):
            up_score += 1
            if m_row[column_index] >= tree:
                break

        for m_row in trees[row_index+1:]:
            down_score += 1
            if m_row[column_index] >= tree:
                break

        max_score = max(max_score, left_score * right_score * up_score * down_score)

print(f"{count=}")
print(f"{max_score=}")
