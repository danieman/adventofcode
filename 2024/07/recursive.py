def calibrate(result, values, gold=False):
    if len(values) == 1:
        return result == values[0]
    if calibrate(result, [values[0]+values[1]] + values[2:], gold):
        return True
    if calibrate(result, [values[0]*values[1]] + values[2:], gold):
        return True
    if gold and calibrate(result, [int(str(values[0])+str(values[1]))] + values[2:], gold):
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

print(silver)
print(gold)
