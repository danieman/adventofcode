from itertools import product


target = 19690720

for noun, verb in product(range(100), range(100)):
    
    nums = [int(n) for n in open('input.txt').read().strip().split(',')]

    nums[1] = noun
    nums[2] = verb

    for i in range(0, len(nums), 4):
        if nums[i] == 1:
            nums[nums[i+3]] = nums[nums[i+1]] + nums[nums[i+2]]
        elif nums[i] == 2:
            nums[nums[i+3]] = nums[nums[i+1]] * nums[nums[i+2]]
        elif nums[i] == 99:
            break

    if nums[0] == target:
        print(100 * noun + verb)
        break
