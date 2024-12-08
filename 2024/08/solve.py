from collections import defaultdict
from itertools import combinations


def get_silver(v, antinodes, xmax, ymax):
    if len(v) == 1: return
    for p, q in combinations(v, 2):
        dx, dy = q[0]-p[0], q[1]-p[1]
        if 0 <= q[0] + dx <= xmax and 0 <= q[1] + dy <= ymax:
            antinodes.add((q[0]+dx, q[1]+dy))
        if 0 <= p[0] - dx <= xmax and 0 <= p[1] - dy <= ymax:
            antinodes.add((p[0]-dx, p[1]-dy))


def get_gold(v, antinodes, xmax, ymax):
    if len(v) == 1: return
    for p, q in combinations(v, 2):
        antinodes.add(p)
        antinodes.add(q)
        dx, dy = q[0]-p[0], q[1]-p[1]
        while 0 <= q[0] + dx <= xmax and 0 <= q[1] + dy <= ymax:
            q = (q[0]+dx, q[1]+dy)
            antinodes.add(q)
        while 0 <= p[0] - dx <= xmax and 0 <= p[1] - dy <= ymax:
            p = (p[0]-dx, p[1]-dy)
            antinodes.add(p)


antennas = defaultdict(list)
with open("input.txt", "r") as f:
    for y, line in enumerate(f.readlines()):
        for x, char in enumerate(line.strip()):
            if char != ".":
                antennas[char].append((x, y))
    xmax, ymax = x, y

# Silver:
silver = set()
for v in antennas.values():
    get_silver(v, silver, xmax, ymax)
print(len(silver))

# Gold
gold = set()
for v in antennas.values():
    get_gold(v, gold, xmax, ymax)
print(len(gold))
