with open("./input.txt") as file:
    list_of_sums = []
    sum = 0
    for line in file:
        if line != "\n":
            sum += int(line.strip())
        else:
            list_of_sums.append(sum)
            sum = 0


print(sorted(list_of_sums))
