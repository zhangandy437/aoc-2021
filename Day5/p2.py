def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

from collections import Counter

inp = input("Day5/in.txt")
d = Counter()

def get_points(f, t):
    if f[0] == t[0] or f[1] == t[1]:
        return Counter((x, y) 
                     for x in range(min(f[0],t[0]), max(f[0],t[0]) + 1) 
                     for y in range(min(f[1],t[1]), max(f[1],t[1]) + 1))
    if abs(f[1] - t[1]) == abs(f[0] - t[0]):
        offx, offy = [-1, 1][f[0] < t[0]], [-1, 1][f[1] < t[1]]
        return Counter((f[0] + i * offx, f[1] + i * offy)
                       for i in range(abs(f[0] - t[0]) + 1))
    return Counter()

for line in inp:
    line = line.split()
    f, t = [int(i) for i in line[0].split(',')], [int(i) for i in line[-1].split(',')]
    d += get_points(f, t)

print(d)
print(sum(1 for key in d.keys() if d[key] > 1))