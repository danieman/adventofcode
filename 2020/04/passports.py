from re import match

def parse_passport(p):
    d = {}
    p.replace("\n", " ")
    fields = p.split()
    for field in fields:
        name, value = field.split(":")
        d[name] = value
    return d

# Task a)
def isvalida(d):
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return all([r in d.keys() for r in required])

# Task b)
def isvalidb(d):
    def parse_height(h):
        try:
            if h[-2:] == "cm":
                return 150 <= int(h[:3]) <= 193
            elif h[-2:] == "in":
                return 59 <= int(h[:2]) <= 76
        except:
            return False

    if not isvalida(d):
        return False

    return all([
        1920 <= int(d["byr"]) <= 2002 and match(r"^\d{4}$", d["byr"]),
        2010 <= int(d["iyr"]) <= 2020 and match(r"^\d{4}$", d["iyr"]),
        2020 <= int(d["eyr"]) <= 2030 and match(r"^\d{4}$", d["eyr"]),
        parse_height(d["hgt"]),
        match(r"^#[0-9a-f]{6}$", d["hcl"]),
        d["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        match(r"^\d{9}$", d["pid"])
    ])


passports = open("input.txt").read().split("\n\n")
print(sum([1 if isvalida(parse_passport(p)) else 0 for p in passports]))
print(sum([1 if isvalidb(parse_passport(p)) else 0 for p in passports]))