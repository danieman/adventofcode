import re

program = [line.strip() for line in open("input.txt").readlines()]


# Task a)
def apply_mask_a(n, mask):
    return "".join([d if d != "X" else n[i] for i, d in enumerate(mask)])

mem = {}
for line in program:
    if line.startswith("mask"):
        mask = line.split()[-1]
    else:
        addr, value = [int(n) for n in re.findall(r"\d+", line)]
        mem[addr] = apply_mask_a(bin(value)[2:].zfill(36), mask)

print(sum([int(v, 2) for v in mem.values()]))


# Task b)
def apply_mask_b(n, mask):
    return "".join([n[i] if d == "0" else mask[i] for i, d in enumerate(mask)])

def generate_all_addr(addr, mask):
    addr = apply_mask_b(addr, mask)
    a = []
    n = addr.count("X")
    for i in range(2 ** n):
        l = list(bin(i)[2:].zfill(n))
        a.append("".join([l.pop(0) if d == "X" else d for d in addr]))
    return a

mem = {}
for line in program:
    if line.startswith("mask"):
        mask = line.split()[-1]
    else:
        addr, value = [int(n) for n in re.findall(r"\d+", line)]
        addr = bin(addr)[2:].zfill(36)
        addrs = generate_all_addr(addr, mask)
        for addr in addrs:
            mem[addr] = value

print(sum([v for v in mem.values()]))