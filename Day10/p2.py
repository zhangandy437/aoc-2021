def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

brack = {'}':'{', ']':'[', ')':'(', '>':'<'}
points = {'{':3, '[':2, '(':1, '<':4}

def get_points(s):
    stack = []
    for c in s:
        if c in brack:
            if stack[-1] != brack[c]:
                return 0
            stack.pop()
        else:
            stack.append(c)
    ans = 0
    # stack = ['<','{','(','[']
    # print(stack)
    while stack:
        c = stack.pop()
        ans *= 5
        ans += points[c]
        # print(ans)
    return ans

points = [i for i in sorted([get_points(line) for line in input('Day10/in.txt')]) if i]
n = len(points)
print(points[n // 2])
