def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines[0]

xs, ys = [[int(j) for j in i[2:].split('..')] for i in input('Day17/in.txt')[13:].split(', ')]

def test(dx, dy):
    x, y = 0, 0
    while x <= max(xs) and y >= min(ys):
        if min(xs) <= x <= max(xs) and min(ys) <= y <= max(ys): return True
        x, y = x + dx, y + dy
        dx, dy = dx - int(dx > 0), dy - 1
    
    return False

print(sum(int(test(i, j)) for i in range(max(xs) + 1) for j in range(min(ys), 1000)))