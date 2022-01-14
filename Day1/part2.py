def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return list(map(lambda x: int(x), lines))

nums = input("/Users/andyzhang/Documents/sandbox/python/adventofcode2021/Day1/in1.txt")
last = float('inf')
ans = 0
for i in range(len(nums)):
    cur = sum(nums[i:i+3])
    ans += cur > last
    last = cur
print(ans)