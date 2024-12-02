def is_safe(seq):
    if seq[0] == seq[-1]: 
        return False
    sign = 1 if seq[0] < seq[-1] else -1
    for i in range(len(seq) - 1):
        diff = (seq[i + 1] - seq[i]) * sign
        if not (1 <= diff <= 3):
            return False
    return True


def is_safe_mod(seq):
    for i in range(len(seq)):
        seq_copy = seq.copy()
        seq_copy.pop(i)
        if is_safe(seq_copy):
            return True
    return False


with open("input.txt", "r") as f:
    silver = []
    gold = []
    for line in f.readlines():
        seq = [int(n) for n in line.strip().split()]
        if is_safe(seq):
            silver.append(seq)
            gold.append(seq)
        elif is_safe_mod(seq):
            gold.append(seq)

# Silver star:
print(len(silver))

# Gold star:
print(len(gold))
