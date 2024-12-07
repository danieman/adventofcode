from itertools import cycle


def is_loop(pos, obstacles, silver=False):
    """Dirty function. Returns a set when silver=True, and a boolean otherwise."""
    directions = cycle([(0, -1), (1, 0), (0, 1), (-1, 0)])
    visited = {pos}
    crashes = set()
    
    d = next(directions)
    while True:
        candidate = (pos[0]+d[0], pos[1]+d[1])
        if candidate in obstacles:
            # Guard hits an obstacle, let's turn right
            if (pos, candidate) in crashes:
                # We've been here before, it's a loop!
                return True
            crashes.add((pos, candidate))
            d = next(directions)
            continue
        elif not (0 <= candidate[0] <= xmax and 0 <= candidate[1] <= ymax):
            # Guard is out of bounds, we're done
            if silver:
                print("Visited:", len(visited))
                return visited
            return False
        else:
            # Taking a step forward
            pos = candidate
            if silver: visited.add(pos)


obstacles = set()
with open("input.txt", "r") as f:
    for r, line in enumerate(f.readlines()):
        for c, char in enumerate(line.strip()):
            if char == "#":
                obstacles.add((c, r))
            elif char == "^":
                pos = (c, r)
    xmax, ymax = c, r

# Silver:
path = is_loop(pos, obstacles, True)

# Gold:
possible_obstructions = 0
for coord in list(path - {pos}):
    # Checking to see if placing a new obstacle on the guard's path leads to a loop
    if is_loop(pos, obstacles | {coord}):
        possible_obstructions += 1
print("Gold:", possible_obstructions)
