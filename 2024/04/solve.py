with open("input.txt", "r") as f:
    grid = []
    for line in f.readlines():
        grid.append(line.strip())

rows = len(grid)
cols = len(grid[0])

silver = 0
wins = ["XMAS", "SAMX"]
for r in range(rows):
    for c in range(cols):
        # Horizontal
        if c + 4 <= cols and grid[r][c:c+4] in wins:
            silver += 1
        # Vertical
        if r + 4 <= rows and grid[r][c] + grid[r+1][c] + grid[r+2][c] + grid[r+3][c] in wins:
            silver += 1
        # Positive diagonal
        if c - 3 >= 0 and r + 4 <= rows and grid[r][c] + grid[r+1][c-1] + grid[r+2][c-2] + grid[r+3][c-3] in wins:
            silver += 1
        # Negative diagonal
        if c + 4 <= cols and r + 4 <= rows and grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] + grid[r+3][c+3] in wins:
            silver += 1

print(silver)


# Gold star:
gold = 0
wins = ["SM", "MS"]
for r in range(1, rows-1):
    for c in range(1, cols-1):
        if grid[r][c] != "A":
            continue
        if grid[r-1][c+1] + grid[r+1][c-1] in wins and grid[r-1][c-1] + grid[r+1][c+1] in wins:
            gold += 1

print(gold)
