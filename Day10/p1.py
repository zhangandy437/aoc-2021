def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

brack = {'}':'{', ']':'[', ')':'(', '>':'<'}
points = {'}':1197, ']':57, ')':3, '>':25137}

def get_points(s):
    stack = []
    for c in s:
        if c in brack:
            if stack[-1] != brack[c]:
                return points[c]
            stack.pop()
        else:
            stack.append(c)
    return 0

print(sum(get_points(line) for line in input('Day10/in.txt')))
    