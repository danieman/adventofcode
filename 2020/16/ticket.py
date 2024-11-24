from collections import defaultdict

fields = defaultdict(set)
legal_numbers = set()
invalids = []

rules, myticket, nearby = open("input.txt").read().split("\n\n")

rules = rules.split("\n")
for rule in rules:
    field, intervals = rule.split(": ")
    i1, i2 = intervals.split(" or ")
    for interval in [i1, i2]:
        start, end = [int(n) for n in interval.split("-")]
        for i in range(start, end + 1):
            fields[field].add(i)
            legal_numbers.add(i)

myticket = myticket.split("\n")[1]
myticket = [int(n) for n in myticket.split(",")]

valid_tickets = []
nearby = nearby.split("\n")[1:-1]
nearby = [[int(n) for n in line.split(",")] for line in nearby]
for ticket in nearby:
    valid = True
    for value in ticket:
        if value not in legal_numbers:
            valid = False
            invalids.append(value)
    if valid:
        valid_tickets.append(ticket)

# Task a)
print(sum(invalids))

# Task b)
candidates = defaultdict(list)
for i, col in enumerate(zip(myticket, *valid_tickets)):
    for key in fields.keys():
        if all([num in fields[key] for num in col]):
            candidates[i].append(key)

while any([len(val) > 1 for val in candidates.values()]):
    for v1 in candidates.values():
        if len(v1) == 1:
            for v2 in candidates.values():
                if v2 != v1 and v1[0] in v2:
                    v2.remove(v1[0])

indices = [k for k, v in candidates.items() if v[0].startswith("departure")]
result = 1
for i in indices:
    result *= myticket[i]

print(result)
