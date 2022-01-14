def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

inp = [i.split("|")[1].split() for i in input("Day8/in.txt")]

print(inp)

ofse = set([2,4,3,7])
ans = 0
for r in inp:
    for word in r:
        if len(word) in ofse: ans += 1
print(ans)