from collections import defaultdict
from math import prod

def find_edges(tile):
    """Takes in a tile, returns the tile ID and a list of edges."""
    lines = tile.split("\n")
    tile_id = lines[0].split()[-1][:-1]
    edges = []
    edges.append(lines[1])
    edges.append(lines[1][::-1])
    edges.append(lines[-1])
    edges.append(lines[-1][::-1])
    left = "".join([l[0] for l in lines[1:]])
    edges.append(left)
    edges.append(left[::-1])
    right = "".join([l[-1] for l in lines[1:]])
    edges.append(right)
    edges.append(right[::-1])
    return tile_id, edges

tiles = open("input.txt").read().strip().split("\n\n")

connections = defaultdict(list)

for tile in tiles:
    tile_id, edges = find_edges(tile)
    for edge in edges:
        connections[edge].append(tile_id)

neighbours = defaultdict(int)

for tile_ids in connections.values():
    if len(tile_ids) == 2:
        for tile_id in tile_ids:
            neighbours[tile_id] += 1

corners = []

for tile_id, count in neighbours.items():
    if count == 4:
        corners.append(int(tile_id))

print(prod(corners))