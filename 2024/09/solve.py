from collections import deque


def silver(files, free_space, raw_disk):
    i = 0
    compact = []
    while raw_disk:
        try:
            for _ in range(files[i]):
                compact.append(raw_disk.popleft())
            for _ in range(free_space[i]):
                compact.append(raw_disk.pop())
        except IndexError:        
            # raw_disk is exhausted
            pass
        i += 1

    silver = 0
    for i, n in enumerate(compact):
        silver += i * n

    return silver


def gold(files, free_space, raw_disk):
    rawraw = [None] * (sum(files) + sum(free_space))
    indices = {}
    idx = n = 0
    while n < len(files) - 1:
        indices[n] = idx
        for _ in range(files[n]):
            rawraw[idx] = n
            idx += 1
        for _ in range(free_space[n]):
            idx += 1
        n += 1
    indices[n] = idx    
    for _ in range(files[n]):
        rawraw[idx] = n
        idx += 1

    #print(rawraw)
    
    subtract = 0
    max_blocks = len(files) - 1
    for f in range(max_blocks, 0, -1):
        print("\rDoing block number", f, end="")
        n = files[f]
        start = indices[f]
        idx = find_first_available(rawraw, n, start)
        if idx == -1 or idx >= start: continue
        for i in range(start, start + n):
            subtract += i * f
        #for i, v in enumerate(rawraw):
        #    if v == f:
        #        rawraw[i] = None
        for i in range(idx, idx + n):
            rawraw[i] = f
   #     print(rawraw)
    gold = 0
    for i, n in enumerate(rawraw):
        if n: gold += i * n
    gold -= subtract
    return gold


def find_first_available(arr, length, start):
    """Given an array of ints, find first run of `length` consecutive zeroes,
    and return the index of the first zero.
    Return -1 if no such consecutive run is found."""
    for i in range(start - length + 1):
        if all(n is None for n in arr[i:i+length]):
            return i
    return -1


with open("input.txt", "r") as f:
    text = f.read().strip()
    #text = "2333133121414131402"
    files = [int(n) for n in text[0::2]]
    free_space = [int(n) for n in text[1::2]]

raw_disk = deque()
for i, n in enumerate(files):
    raw_disk.extend([i] * n)

print("Silver:", silver(files, free_space, raw_disk))
print("Gold:", gold(files, free_space, raw_disk))
