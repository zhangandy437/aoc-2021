def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

from collections import Counter

crabs = [int(i) for i in input("Day7/in.txt")[0].split(',')]
crabs.sort()
crabbies = Counter(crabs)

l, r = min(crabs), max(crabs)
a = round(sum(crabs) / len(crabs))
m = crabs[len(crabs) // 2]

def min_fuel(to):
    return sum(abs(i - to) * crabbies[i] for i in crabbies.keys())
        
print(a, m)
print(min((min_fuel(i),i) for i in range(min(a, m), max(a, m) + 1)))