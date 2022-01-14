def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines[0]

xs, ys = [[int(j) for j in i[2:].split('..')] for i in input('Day17/in.txt')[13:].split(', ')]

y1 = abs(min(ys))

print(y1 * ((y1 - 1) / 2))