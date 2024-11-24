import regex


regs = {}
rules, lines = open("input.txt").read().split("\n\n")
rules = rules.split("\n")
lines = lines.strip().split("\n")

for rule in rules:
    n, r = rule.split(": ")
    regs[int(n)] = r


# Part one
def build_regex_a(rule, regs):
    if '"' in rule:
        return rule[1]
    
    elif "|" in rule:
        r1, r2 = rule.split(" | ")
        r = f"({build_regex_a(r1, regs)}|{build_regex_a(r2, regs)})"

    else:
        r = ""
        refs = [int(n) for n in rule.split()]
        for ref in refs:
            r += build_regex_a(regs[ref], regs)
    
    return r

r = build_regex_a(regs[0], regs)
print(sum([1 for line in lines if regex.match(f"^{r}$", line)]))


# Part two
def build_regex_b(n, regs):
    if n == 8:
        return f"(?:{build_regex_b(42, regs)})+"
    elif n == 11:
        a = build_regex_b(42, regs)
        b = build_regex_b(31, regs)
        return f"({a}(?>{a}{b}|(?1))*{b})"

    rule = regs[n]
    if '"' in rule:
        return rule[1]
    
    elif "|" in rule:
        r1, r2 = rule.split(" | ")
        r1 = [int(r) for r in r1.split()]
        r2 = [int(r) for r in r2.split()]
        r = f'(?:{"".join(build_regex_b(r, regs) for r in r1)}|'
        r += f'{"".join(build_regex_b(r, regs) for r in r2)})'

    else:
        r = ""
        refs = [int(n) for n in rule.split()]
        for ref in refs:
            r += build_regex_b(ref, regs)
    
    return r

regs[8] = "42 | 42 8"
regs[11] = "42 31 | 42 11 31"
r = build_regex_b(0, regs)
print(sum([1 for line in lines if regex.match(f"^{r}$", line)]))