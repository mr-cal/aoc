score: int = 0
badge_score: int = 0
badge_list = []

with open("./input.txt") as file:
    for index, line in enumerate(file):
        line = line.strip()
        left = line[int(len(line)/2):]
        right = line[:int(len(line)/2)]

        badge_list.append(line)

        duplicates = set(left)
        duplicates.intersection_update(set(right))
        duplicate = duplicates.pop()

        if duplicate == duplicate.lower():
            score += ord(duplicate) - 96
        else:
            score += ord(duplicate) - 38

        # find badge for each group of 3 elves
        if index % 3 == 2 and len(badge_list) != 0:
            duplicate_badges = set(badge_list[0])
            for contents in badge_list[1:]:
                duplicate_badges.intersection_update(set(contents))
            badge = duplicate_badges.pop()
            badge_list = []
            if badge == badge.lower():
                badge_score += ord(badge) - 96
            else:
                badge_score += ord(badge) - 38

print(f"{score=}")
print(f"{badge_score=}")
