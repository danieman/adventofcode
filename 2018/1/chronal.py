file = [int(line.strip()) for line in open('input.txt')]
frequencies = set()
freq = 0

def looplist(loop=True):
    global file, freq, frequencies
    while True:
        for line in file:
            freq += line
            if freq in frequencies:
                return freq
            else:
                frequencies.add(freq)
        if loop == False:
            return freq

# a)
print(f'a): {looplist(False)}')
# Solution: 477

# b)
print(f'b): {looplist()}')
# Solution: 390 (137 rounds)