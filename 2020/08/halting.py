from copy import deepcopy

instructions = [[ins, eval(n)] for ins, n in (line.strip().split() for line in open("input.txt").readlines())]

# Task a)
seen = set()
idx = 0
acc = 0
while True:
    if idx in seen:
        break
    seen.add(idx)
    ins, n = instructions[idx]
    if ins == "acc":
        acc += n
        idx += 1
    elif ins == "jmp":
        idx += n
    else:
        idx += 1

print(acc)


# Task b)
l = len(instructions)
for i in range(l):
    ins, _ = instructions[i]
    if ins not in ["jmp", "nop"]:
        continue

    shadow = deepcopy(instructions)
    shadow[i][0] = "jmp" if instructions[i][0] == "nop" else "nop"
    seen = set()
    idx = 0
    acc = 0
    finished = False
    while True:
        if idx in seen:
            break
        seen.add(idx)
        ins, n = shadow[idx]
        if ins == "acc":
            acc += n
            idx += 1
        elif ins == "jmp":
            idx += n
        else:
            idx += 1
        if idx == l:
            finished = True
            break
    if finished:
        print(f"Changed instruction #{i} from \"{instructions[i][0]}\" to \"{shadow[i][0]}\".")
        print(f"Accumulator contains the value {acc}.")
        break