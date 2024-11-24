from collections import defaultdict

adapters = [0] + sorted([int(n) for n in open("input.txt").readlines()])
adapters.append(max(adapters) + 3)
diff = defaultdict(int)

# Task a)
for i, n in enumerate(adapters[1:]):
    prev = adapters[i]
    diff[n - prev] += 1

print(diff[1] * diff[3])

# Task b)
lookup = {0: 1}
for n in adapters[1:]:
    ways = 0
    for x in range(n - 3, n):
        ways += lookup.get(x, 0)
    lookup[n] = ways

print(lookup[max(adapters)])