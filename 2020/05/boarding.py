from collections import defaultdict


def seatid(seat):
    seat = seat.translate(str.maketrans("BFLR", "1001"))
    row, col = int(seat[:7], 2), int(seat[7:], 2)
    return row * 8 + col, row, col


seats = [line.strip() for line in open("input.txt").readlines()]

# Task a)
print(max([seatid(seat)[0] for seat in seats]))

# Task b)
d = defaultdict(list)
for seat in seats:
    _, row, col = seatid(seat)
    d[row].append(col)

for k, v in d.items():
    if len(v) != 8 and k != max(d) and k != min(d):
        for i in range(8):
            if i not in v:
                print(k * 8 + i)