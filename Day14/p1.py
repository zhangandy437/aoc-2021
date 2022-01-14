from collections import Counter


def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

inp = input('Day14/in.txt')
template, rules = inp[0], dict(i.split(' -> ') for i in inp[2:])

pairs = Counter(map(str.__add__, template, template[1:]))
chars = Counter(template)

print(pairs)

for _ in range(40):
    for (a, b), c in pairs.copy().items(): # iterate over copy
        x = rules[a + b] # num of ab or the key
        pairs[a+b] -= c # remove the key since its changing
        pairs[a+x] += c # add the changes
        pairs[x+b] += c # add the changes
        chars[x] += c   # add number of characters total
    # print(pairs, chars)
    
items = list(chars.most_common())
print(items)
print(items[0][1] - items[-1][1])