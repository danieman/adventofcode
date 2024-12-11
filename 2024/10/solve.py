def calculate_score(pos, grid, xmax, ymax):
    x, y = pos
    n = grid[y][x]
    if n == 9: 
        return {pos}, 1
    
    candidates = []
    if 0 <= x - 1: candidates.append((x-1, y))
    if x + 1 < xmax: candidates.append((x+1, y))
    if 0 <= y - 1: candidates.append((x, y-1))
    if y + 1 < ymax: candidates.append((x, y+1))

    if n + 1 not in [grid[j][i] for i, j in candidates]:
        return set(), 0

    peaks = set()
    trails = 0
    for p in candidates:
        if grid[p[1]][p[0]] == n + 1:
            v, t= calculate_score(p, grid, xmax, ymax)
            peaks |= v
            trails += t

    return peaks, trails


with open("input.txt", "r") as f:
    grid = []
    trailheads = []
    for i, line in enumerate(f.readlines()):
        row = []
        for j, c in enumerate(line.strip()):
            row.append(int(c))
            if c == "0":
                trailheads.append((j, i))
        grid.append(row)
    xmax, ymax = len(grid[0]), len(grid)

silver = gold = 0
for pos in trailheads:
    p, t = calculate_score(pos, grid, xmax, ymax)
    silver += len(p)
    gold += t
#    print(pos, len(p), t, p)

print(silver)
print(gold)

