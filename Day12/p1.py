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

def dfs(node, visited, path):
    if node == 'end': 
        print(path)
        return 1
    ans = 0
    for n in graph[node]:
        if n.islower() and n in visited:
            continue
        if (node, n) in visited: continue
        if n.islower():
            visited.add(n)
        visited.add((node, n))
        ans += dfs(n, visited, path + [n])
        visited.remove((node, n))
        if n.islower():
            visited.remove(n)
    return ans
from collections import Counter
d = Counter()
d['start'] = 2
print(dfs('start', d, ['start']))