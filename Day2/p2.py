def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return [i.split(' ') for i in lines]

dirs = input("/Users/andyzhang/Documents/sandbox/python/adventofcode2021/Day2/in.txt")

h, d, a = 0, 0, 0

for di, m in dirs:
    m = int(m)
    if di == 'forward':
        h += m
        d += a * m
    elif di == 'down':
        a += m
    else:
        a -= m
print(h * d)