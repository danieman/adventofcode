from math import prod

terrain = [line.strip() for line in open("input.txt").readlines()]

result = []
end = len(terrain[0])
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

for right, down in slopes:
    x, y = 0, 0
    trees = 0
    for _ in range(0, len(terrain), down):
        if terrain[y][x] == "#":
            trees += 1
        x = (x + right) % end
        y += down
    result.append(trees)

print(result)
print(prod(result))