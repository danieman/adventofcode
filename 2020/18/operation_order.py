class Int(int):
    def __add__(self, other):
        return Int(int(self) * int(other))
    def __mul__(self, other):
        return Int(int(self) + int(other))

def find_exprs(line):
    intervals = []
    start = end = None
    level = 0
    for i, c in enumerate(line):
        if c == "(":
            if level == 0:
                start = i + 1
            level += 1
        elif c == ")":
            if level == 1:
                end = i
                intervals.append((start, end))
            level -= 1
    return intervals

def solve(line, part="a"):
    intervals = find_exprs(line)
    if intervals:
        out = ""
        i = 0
        for start, end in intervals:
            out += line[i:start - 1]
            out += str(solve(line[start:end], part))
            i = end + 1
        out += line[i:]
        line = out
    if part == "a":
        return a(line)
    else:
        return b(line)

def a(s):
    ops = s.split()
    total = int(ops[0])
    for i in range(1, len(ops), 2):
        if ops[i] == "+":
            total += int(ops[i + 1])
        elif ops[i] == "*":
            total *= int(ops[i + 1])
    return total

def b(s):
    ops = s.split()
    out = ""
    total = Int(ops[0])
    for element in ops:
        if element == "+":
            out += "*"
        elif element == "*":
            out += "+"
        else:
            out += f"Int({element})"
    return eval(out)


# tests = [
#     "1 + (2 * 3) + (4 * (5 + 6))",
#     "2 * 3 + (4 * 5)",
#     "5 + (8 * 3 + 9 + 3 * 4 * 3)",
#     "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
#     "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
# ]

# for test in tests:
#     print(solve(test))
# for test in tests:
#     print(solve(test, "b"))

lines = [line.strip() for line in open("input.txt").readlines()]
print(sum([solve(line) for line in lines]))
print(sum([solve(line, "b") for line in lines]))