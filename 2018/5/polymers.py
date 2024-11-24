def find_length(s):
    while True:
        length = len(s)
        for i in range(len(s)-2, -1, -1):
            if s[i].swapcase() == s[i+1]:
                del s[i:i+2]
        if length == len(s):
            return length
        else:
            length = len(s)

s = list(open('input.txt').read().strip())
chars = {l.lower(): 0 for l in set(s)}

# a)
print(find_length(s))

# b)
for c in chars.keys():
    pol = [l for l in s if l.lower() != c]
    chars[c] = find_length(pol)

print(min(chars.values()))