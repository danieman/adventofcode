from itertools import product


def calibrate(result, values, gold=False):
    ops = "+*|" if gold else "+*"
    operators = product(ops, repeat=len(values)-1)
    for seq in operators:
        total = values[0]
        for i in range(len(values)-1):
            if seq[i] == "+":
                total += values[i+1]
            elif seq[i] == "*":
                total *= values[i+1]
            elif seq[i] == "|":
                total = int(str(total) + str(values[i+1]))
            if total > result:
                break
        if total == result:
            return True
    return False


silver = gold = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        result, values = line.strip().split(": ")
        result = int(result)
        values = [int(n) for n in values.split()]
        if calibrate(result, values):
            silver += result
            gold += result
        elif calibrate(result, values, gold=True):
            gold += result

# Silver
print(silver)
print(gold)
