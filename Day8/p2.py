def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

lines = input("Day8/in.txt")
ofse = {2:1,4:4,3:7,7:8}

def decode(left):
    d = {}
    r = {}
    fives = []
    sixes = []
    for dig in left:
        if len(dig) in ofse:
            d[dig] = ofse[len(dig)]
            r[ofse[len(dig)]] = dig
        elif len(dig) == 5:
            fives.append(dig)
        elif len(dig) == 6:
            sixes.append(dig)
    for dig in fives:
        if dig not in d:
            if len(set(r[7]) & set(dig)) == 3:
                d[dig] = 3 
            elif len(set(r[4]) & set(dig)) == 2:
                d[dig] = 2
            elif len(set(r[7]) & set(dig)) == 2:
                d[dig] = 5 
    for dig in sixes:
        if dig not in d:
            if len(set(r[4]) & set(dig)) == 4:
                d[dig] = 9
            elif len(set(r[7]) & set(dig)) == 3:
                d[dig] = 0
            else:
                d[dig] = 6
    return d

ans = 0
for line in lines:
    left, right = line.split('|')
    left, right = [''.join(sorted(i)) for i in left.split()], [''.join(sorted(i)) for i in right.split()]
    
    d = decode(left)
    output = 0
    for dig in right:
        output *= 10
        output += d[dig]
    ans += output
    
print(ans)