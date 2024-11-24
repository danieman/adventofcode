import re

def find_coords(left, top, width, height):
    coords = set()
    for i in range(width):
        for j in range(height):
            coords.add( (left+i, top+j) )
    return coords

claimed_twice = set()
claimed_once = set()
claims = {}

for line in open('input.txt'):
    id, left, top, width, height = map(int, re.findall(r'\d+', line))
    coords = find_coords(left, top, width, height)
    claims[id] = coords
    for coord in coords:
        if coord in claimed_twice:
            continue
        elif coord in claimed_once:
            claimed_twice.add(coord)
        else:
            claimed_once.add(coord)

# a)
print(len(claimed_twice))
# Solution: 118322

# b)
def find_single_claim():
    for k,v in claims.items():
        for coord in v:
            if coord in claimed_twice:
                break
        else:
            return k

print(find_single_claim())
# Solution: 1178