def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

heights = [[int(i) for i in line] for line in input('Day9/in.txt')]
n, m = len(heights), len(heights[0])

s = set()
basins = []

def dfs(x, y):
    if 0 <= x < len(heights) and 0 <= y < len(heights[1]) and (x, y) not in s and heights[x][y] != 9:
        s.add((x, y))
        out = 1
        for l, r in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            out += dfs(x + l, y + r)
        return out
    return 0

ans = 0
for r in range(n):
    for c in range(m):
        height = heights[r][c]
        if height == 9 or (r, c) in s: continue
        basins.append(dfs(r, c))
basins.sort()

print(basins[-1] * basins[-2] * basins[-3])