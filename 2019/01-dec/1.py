def required_fuel(mass):
    return mass//3 - 2


def recursive_fuel(mass):
    fuel = required_fuel(mass)
    if fuel <= 0:
        return 0
    else:
        return fuel + recursive_fuel(fuel)


modules = [int(line.strip()) for line in open('input.txt').readlines()]

# 1a)
print(sum([required_fuel(m) for m in modules]))

# 1b)
print(sum([recursive_fuel(m) for m in modules]))