from collections import defaultdict

contains = defaultdict(list)
lines = [line.strip() for line in open("input.txt").readlines()]
for line in lines:
    color, containables = line.strip(".").split(" bags contain ")
    if containables == "no other bags":
        contains[color] = []
        continue
    c = containables.split(", ")
    for b in c:
        n, b1, b2, _ = b.split()
        contains[color].append((n, f"{b1} {b2}"))

contained_by = defaultdict(list)
for k, v in contains.items():
    for _, color in v:
        contained_by[color].append(k)


# Task a)
result = set()
to_check = ["shiny gold"]
while to_check:
    color = to_check.pop(0)
    result.add(color)
    for c in contained_by[color]:
        to_check.append(c)

print(f"a) {len(result) - 1} colors can hold a shiny gold bag.")


# Task b)
def total_bags(color):
    if not contains[color]:
        return 1   
    total = 1
    for n, c in contains[color]:
        total += (int(n) * total_bags(c))    
    return total

print(f"b) A shiny gold bag holds {total_bags('shiny gold') - 1} other bags.")