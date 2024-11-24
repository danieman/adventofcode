def isvalid(lines, improved=False):
    valids = 0
    for n, c, p in lines:
        low, high = [int(i) for i in n.split("-")]
        c = c[0]
        if improved:
            if (p[low - 1] == c) ^ (p[high - 1] == c):
                valids += 1
        else:
            if low <= p.count(c) <= high:
                valids += 1
    return valids


with open("input.txt") as f:
    lines = [line.strip().split() for line in f.readlines()]

print(isvalid(lines))
print(isvalid(lines, improved=True))