PREAMBLE = 25

inputs = [int(n) for n in open("input.txt").readlines()]

# Task a)
for idx in range(PREAMBLE, len(inputs)):
    valid = False
    n = inputs[idx]
    for i, x in enumerate(inputs[idx - PREAMBLE:idx - 1], start=idx - PREAMBLE):
        if (n - x) in inputs[i + 1:idx]:
            valid = True
            break
    
    if not valid:
        print(n)
        break

# Task b)
invalid = n
for i in range(len(inputs)):
    total = 0
    idx = i
    while total < invalid:
        total += inputs[idx]
        idx += 1
        if total == invalid:
            numbers = inputs[i:idx]
            print(max(numbers) + min(numbers))
            exit()