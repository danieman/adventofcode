from collections import Counter

twos, threes = 0, 0
lines = [line.strip() for line in open('input.txt')]

# a)
for line in lines:
    c = Counter(line)
    counts = [c[letter] for letter in set(line)]
    if 2 in counts:
        twos += 1
    if 3 in counts:
        threes += 1 

print(twos*threes)

# b)
def strcmp(s1, s2):
    """Returns True if s1 and s2 differs by exactly one character, else False."""
    if len(s1) != len(s2): 
        return False
    errors = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            errors += 1
            if errors > 1:
                return False
    return True if errors == 1 else False

for i in range(len(lines)-1):
    for j in range(i+1, len(lines)):
        if strcmp(lines[i], lines[j]):
            print(''.join([l1 for l1, l2 in zip(lines[i], lines[j]) if l1 == l2 ]))
