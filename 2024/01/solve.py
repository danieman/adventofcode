with open("input.txt", "r") as f:
    left, right = [], []
    for line in f.readlines():
        l, r = line.strip().split()
        left.append(int(l))
        right.append(int(r))
    left.sort()
    right.sort()


# Silver star:
total = 0
for l, r in zip(left, right):
    total += abs(l - r)

print("Silver:")
print(total)


# Gold star:
sim_score = 0
for l in left:
    sim_score += (l * right.count(l))

print("\nGold:")
print(sim_score)
