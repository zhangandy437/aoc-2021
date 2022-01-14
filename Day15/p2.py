def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return [[int(i) for i in l] for l in lines]

maze = input('Day15/in.txt')

n = len(maze)

def change(n,k):
    if n + k > 9:
        return (n + k + 1) % 10
    return n + k

def get(x, y):
    n = len(maze)
    k = x // n + y // n
    return change(maze[x % n][y % n], k)
    
def manhat(x, y):
    return len(maze) * 5 - x - 1 + len(maze) * 5 - y - 1

def inbounds(x, y):
    n = len(maze)
    return 0 <= x < (n * 5) and 0 <= y < (n * 5)

import heapq as hq

# hold distances
closed = {(0,0): 0}
# heuristic, x, y
q = [(manhat(0,0), 0, 0)]
while q:
    cost, x, y = hq.heappop(q)
    if x == n * 5 - 1 and y == n * 5 - 1: 
        print(closed[(x, y)])
        break
    
    for l, r in [(-1,0),(1,0),(0,-1),(0,1)]:
        l, r = l + x, r + y
        if inbounds(l, r):
            if (l, r) not in closed or closed[(l, r)] > closed[(x, y)] + get(l, r):
                closed[(l, r)] = closed[(x, y)] + get(l, r)
                q.append((closed[(l, r)] + manhat(l, r), l, r))
    q.sort()