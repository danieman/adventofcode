from copy import deepcopy

grid = [list(line.strip()) for line in open("input.txt").readlines()]
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
xlimit = len(grid[0])
ylimit = len(grid)

# Task a)
def occupied_neighbours(coords, grid):
    visible = 0
    for x, y in directions:
        xpos, ypos = coords
        if 0 <= xpos + x < xlimit and 0 <= ypos + y < ylimit:
            if grid[ypos + y][xpos + x] == "#":
                visible += 1
    return visible
    
while True:
    old = deepcopy(grid)
    for y, row in enumerate(old):
        for x, col in enumerate(row):
            occupied = occupied_neighbours([x, y], old)
            if old[y][x] == "#" and occupied >= 4:
                grid[y][x] = "L"
            elif old[y][x] == "L" and occupied == 0:
                grid[y][x] = "#"
    if old == grid:
        break

print(sum([line.count("#") for line in grid]))

# Task b)
def count_visible(coords, grid):
    visible = 0
    for x, y in directions:
        xpos, ypos = coords
        while 0 <= xpos + x < xlimit and 0 <= ypos + y < ylimit:
            xpos += x
            ypos += y
            if grid[ypos][xpos] == "#":
                visible += 1
                break
            if grid[ypos][xpos] == "L":
                break
    return visible

grid = [list(line.strip()) for line in open("input.txt").readlines()]
while True:
    old = deepcopy(grid)
    for y, row in enumerate(old):
        for x, col in enumerate(row):
            occupied = count_visible([x, y], old)
            if old[y][x] == "#" and occupied >= 5:
                grid[y][x] = "L"
            elif old[y][x] == "L" and occupied == 0:
                grid[y][x] = "#" 
    if old == grid:
        break

print(sum([line.count("#") for line in grid]))