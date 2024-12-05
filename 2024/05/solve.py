from collections import defaultdict


def check_update(update, rules):
    for i in range(len(update)-1):
        if update[i] in rules[update[i+1]]:
            return False
    return True


def fix_update(update, rules):
    # The good, old bubble sort approach
    i, stop = 0, len(update) - 1
    while stop:
        if update[i] in rules[update[i+1]]:
            update[i], update[i+1] = update[i+1], update[i]
        i += 1
        if i == stop:
            i = 0
            stop -= 1
    return update


with open("input.txt", "r") as f:
    rules, updates = f.read().split("\n\n")

updates = [row.strip().split(",") for row in updates.splitlines()]
rulebook = defaultdict(list)
for rule in rules.splitlines():
    first, last = rule.split("|")
    rulebook[first].append(last)

silver = gold = 0
for update in updates:
    if check_update(update, rulebook):
        silver += int(update[len(update)//2])
    else:
        fixed_update = fix_update(update, rulebook)
        gold += int(fixed_update[len(fixed_update)//2])

print(silver)
print(gold)
