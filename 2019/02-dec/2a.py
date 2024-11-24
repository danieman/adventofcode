nums = [int(n) for n in open('input.txt').read().strip().split(',')]

nums[1] = 12
nums[2] = 2

for i in range(0, len(nums), 4):
    if nums[i] == 1:
        nums[nums[i+3]] = nums[nums[i+1]] + nums[nums[i+2]]
    elif nums[i] == 2:
        nums[nums[i+3]] = nums[nums[i+1]] * nums[nums[i+2]]
    elif nums[i] == 99:
        break
    else:
        print(f"Rart tall: {nums[i]}")

print(nums)