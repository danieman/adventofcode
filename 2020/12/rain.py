HEADINGS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
instructions = [line.strip() for line in open("input.txt").readlines()]

# Task a)
h = 0  # Heading number
pos = [0, 0]
for instruction in instructions:
    action, amount = instruction[0], int(instruction[1:])
    if action == "N":
        pos[1] -= amount
    elif action == "S":
        pos[1] += amount
    elif action == "E":
        pos[0] += amount
    elif action == "W":
        pos[0] -= amount
    elif action == "L":
        h = (h - amount // 90) % 4
    elif action == "R":
        h = (h + amount // 90) % 4
    elif action == "F":
        pos[0] += HEADINGS[h][0] * amount
        pos[1] += HEADINGS[h][1] * amount
    
print(abs(pos[0]) + abs(pos[1]))

# Task b)
pos = [0, 0]
wp = [10, -1]
for instruction in instructions:
    action, amount = instruction[0], int(instruction[1:])
    if action == "N":
        wp[1] -= amount
    elif action == "S":
        wp[1] += amount
    elif action == "E":
        wp[0] += amount
    elif action == "W":
        wp[0] -= amount
    elif action == "L":
        for _ in range(amount // 90):
            wp[0], wp[1] = wp[1], -wp[0]
    elif action == "R":
        for _ in range(amount // 90):
            wp[0], wp[1] = -wp[1], wp[0]
    elif action == "F":
        pos[0] += wp[0] * amount
        pos[1] += wp[1] * amount
    
print(abs(pos[0]) + abs(pos[1]))