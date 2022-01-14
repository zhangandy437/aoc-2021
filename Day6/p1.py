def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

from collections import Counter
inp = input("Day6/in.txt")

fish = Counter(int(i) for i in inp[0].split(','))
print(fish)

addq = [0,0]

for day in range(256):
    tick = day % 7
    addq.append(fish[tick])
    fish[tick] += addq[-3]

print(fish)
print(sum(fish.values()) + addq[-1] + addq[-2])