def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return [i.split('-') for i in lines]

edges = input('Day12/in.txt')
graph = {}

for l, r in edges:
    graph.setdefault(l, []).append(r)
    graph.setdefault(r, []).append(l)

def dfs(node, visited, path, twice):
    if node == 'end': 
        print(path)
        return 1
    ans = 0
    for n in graph[node]:
        if n.islower() and visited[n] > twice:
            continue
        # if visited[(node, n)]: continue
        # if n.islower():
        visited[n] += 1
        # visited[(node, n)] += 1
        # print(visited, twice)
        ans += dfs(n, visited, path + [n], False if not twice else not n.islower() or visited[n] < 2)
        # visited[(node, n)] -= 1
        # if n.islower():
        visited[n] -= 1
    return ans
from collections import Counter
d = Counter()
d['start'] = 2
print(dfs('start', d, ['start'], True))