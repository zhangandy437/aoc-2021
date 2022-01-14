def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return list(map(lambda x: int(x), lines))

nums = input("/Users/andyzhang/Documents/sandbox/python/adventofcode2021/Day1/in1.txt")

last = float('inf')
ans = 0
for num in nums:
    ans += last < num
    last = num
print(ans)