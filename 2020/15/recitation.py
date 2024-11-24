from collections import defaultdict

NUMBERS = [6, 19, 0, 5, 7, 13, 1]

def recite(numbers, stop):
    last_spoken = defaultdict(list, {n:[i] for i, n in enumerate(NUMBERS, start=1)})
    turn = len(NUMBERS) + 1
    prev_is_new = True
    while turn <= stop:
        if prev_is_new:
            number = 0
            if number in last_spoken.keys():
                prev_is_new = False
            last_spoken[number].append(turn)
        else:
            number = (turn - 1) - last_spoken[number][-2]
            if number not in last_spoken.keys():
                prev_is_new = True
            last_spoken[number].append(turn)
        turn += 1
    return number

# Task a)
print(recite(NUMBERS, 2020))
# Task b)
print(recite(NUMBERS, 3 * 10 ** 7))