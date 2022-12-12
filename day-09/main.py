from collections import namedtuple

Move = namedtuple("Move", ["direction", "distance"])
head_moves = []
with open("./input.txt", encoding="utf8") as file:
    for line in file:
        print(*line.strip().split(" "))
        head_moves.append(Move(*line.strip().split(" ")))

Point = namedtuple("Point", ["x", "y"])
tails = [ [Point(0,0)] for _ in range(10)]

def head_touches_tail(m_head: Point, m_tail: Point):
    """Check if the head and tail are touching (adjacent)."""
    if abs(m_head.x-m_tail.x) <= 1 and abs(m_head.y-m_tail.y) <= 1:
        return True
    return False

for move in head_moves:
    # move head
    if move.direction == "U":
        tails[0].append(Point(tails[0][-1].x, tails[0][-1].y + int(move.distance)))
    elif move.direction == "D":
        tails[0].append(Point(tails[0][-1].x, tails[0][-1].y - int(move.distance)))
    elif move.direction == "L":
        tails[0].append(Point(tails[0][-1].x - int(move.distance), tails[0][-1].y))
    elif move.direction == "R":
        tails[0].append(Point(tails[0][-1].x + int(move.distance), tails[0][-1].y))

    # move each tail except the first tail (the head)
    for index, tail in enumerate(tails[1:]):
        while not head_touches_tail(tails[index][-1], tail[-1]):
            if tail[-1].x < tails[index][-1].x:
                tail_next_x = tail[-1].x + 1
            elif tail[-1].x > tails[index][-1].x:
                tail_next_x = tail[-1].x - 1
            else:
                tail_next_x = tail[-1].x

            if tail[-1].y < tails[index][-1].y:
                tail_next_y = tail[-1].y + 1
            elif tail[-1].y > tails[index][-1].y:
                tail_next_y = tail[-1].y - 1
            else:
                tail_next_y = tail[-1].y

            tail.append(Point(tail_next_x, tail_next_y))

for tail in tails:
    print(len(set(tail)))
