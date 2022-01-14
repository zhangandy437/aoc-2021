def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return [i.split(' ') for i in lines]

dirs = input("/Users/andyzhang/Documents/sandbox/python/adventofcode2021/Day2/in.txt")

h, d = 0, 0

for di, m in dirs:
    if di == 'forward':
        h += int(m)
    elif di == 'down':
        d  += int(m)
    else:
        d -= int(m)
print(h * d)