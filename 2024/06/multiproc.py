from functools import partial
from itertools import cycle
from multiprocessing import Pool, cpu_count


def process_coord(coord, pos, obstacles):
    updated_obstacles = obstacles | {coord}
    return is_loop(pos, updated_obstacles)


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
path = list(is_loop(pos, obstacles, True) - {pos})

# Gold:
with Pool(cpu_count()) as pool:
    counts = pool.map(partial(process_coord, pos=pos, obstacles=obstacles), path)
print("Gold:", sum(counts))
