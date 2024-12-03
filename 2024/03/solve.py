import re


with open("input.txt", "r") as f:
    text = f.read()

enabled = True
i, l = 0, len(text)
silver = gold = 0
while i < l - 7:
    if text[i] not in "dm":
        i += 1
        continue
    if text[i:i+7] == "don't()":
        enabled = False
        i += 6
    elif text[i:i+4] == "do()":
        enabled = True
        i += 3
    elif m := re.match(r"mul\((\d+?),(\d+?)\)", text[i:]):
        a, b = m.groups()
        silver += int(a) * int(b)
        if enabled:
            gold += int(a) * int(b)
        i += len(m.group(0))
        continue
    i += 1

# Silver star:
print(silver)

# Gold star:
print(gold)
