def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

nums = input("/Users/andyzhang/Documents/sandbox/python/adventofcode2021/Day3/in.txt")

g, e = 0, 0
count = [0] * len(nums[0])

for num in nums:
    for i in range(len(num)):
        if num[i] == '1': count[i] += 1

n = len(nums)
half = n // 2
count = count[::-1]
for i in range(len(count)):
    if count[i] > half:
        g |= 1 << i
    else:
        e |= 1 << i
print(g, e, g * e)