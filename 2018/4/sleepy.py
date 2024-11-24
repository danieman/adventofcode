from collections import defaultdict

lines = sorted([line.strip() for line in open('input.txt')])

d = defaultdict(lambda: [0]*60)
id, falls_asleep, wakes_up = None, None, None

for line in lines:
    if '#' in line:
        id = line.split()[3][1:]
    elif 'asleep' in line:
        falls_asleep = int(line.split()[1][3:5])
    else:
        wakes_up = int(line.split()[1][3:5])
        for i in range(falls_asleep, wakes_up):
            d[id][i] += 1

# a)
sleepiest_guard, most_minutes_asleep = None, []
for k, v in d.items():
    if sum(v) > sum(most_minutes_asleep):
        sleepiest_guard, most_minutes_asleep = int(k), v

sleepiest_minute = most_minutes_asleep.index(max(most_minutes_asleep))
print(sleepiest_minute*sleepiest_guard)

# b)
max_value = 0
for k, v in d.items():
    if max(v) > max_value:
        max_value = max(v)
        top_sleeper, frequent_minute = int(k), v.index(max_value)

print(top_sleeper*frequent_minute)