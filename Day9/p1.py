def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

heights = [[int(i) for i in line] for line in input('Day9/in.txt')]
n, m = len(heights), len(heights[0])

def get_adj(x, y, n, m):
    adj = []
    for d, f in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if 0 <= x + d < n and 0 <= y + f < m:
            adj.append((x + d, y + f))
    return adj
ans = 0
for r in range(n):
    for c in range(m):
        height = heights[r][c]
        low = True
        for x, y in get_adj(r, c, n, m):
            if heights[x][y] <= height: low = False
        if low: ans += height + 1
print(ans)