from collections import defaultdict

cache = {}

def blinkv2(n, stones, cache):
    s = defaultdict(int)
    for stone in stones:
        s[stone] += 1

    for i in range(n):
        ns = defaultdict(int)
        for k, v in s.items():
            if k in cache:
                for r in cache[k]:
                    ns[r] += v
            else:
                if k == "0":
                    ns["1"] += v
                    cache[k] = ("1", ) 
                elif len(k) % 2 == 0:
                    ns[k[:len(k)//2]] += v
                    ns[str(int(k[len(k)//2:]))] += v
                    cache[k] = (k[:len(k)//2], str(int(k[len(k)//2:])))
                else:
                    ns[str(int(k)*2024)] += v
                    cache[k] = (str(int(k) * 2024), )
        s = ns
    return sum(s.values())



with open("input.txt", "r") as f:
    stones = f.read().strip().split()

# Test cases:
#stones = ["0", "1", "10", "99", "999"]
#stones = ["125", "17"]

# Silver
print(blinkv2(25, stones.copy(), cache))

# Gold
print(blinkv2(75, stones.copy(), cache))
