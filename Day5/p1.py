def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

from collections import Counter

inp = input("Day5/in.txt")
d = Counter()

for line in inp:
    line = line.split()
    f, t = [int(i) for i in line[0].split(',')], [int(i) for i in line[-1].split(',')]
    if f[0] == t[0] or f[1] == t[1]:
        d += Counter((x, y) 
                     for x in range(min(f[0],t[0]), max(f[0],t[0]) + 1) 
                     for y in range(min(f[1],t[1]), max(f[1],t[1]) + 1))

print(d)
print(sum(1 for key in d.keys() if d[key] > 1))