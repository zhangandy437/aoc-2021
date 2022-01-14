def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return [[int(i) for i in line] for line in lines]

board = input('Day11/in.txt')
steps = 1656
# key: string board, value: (num flashed, string next board)
mem = {}

def dup(board):
    return [l[:] for l in board]

def stringify(board):
    return ''.join(''.join(str(i) for i in l) for l in board)

def destring(s):
    n = []
    for i in range(10):
        n.append([int(j) for j in s[i * 10:(i + 1) * 10]])
    return n

def step(board):
    strung = stringify(board)
    if strung in mem:
        n, b = mem[strung]
        return n, destring(b)
    
    flash = []
    flashed = set()
    for r in range(10):
        for c in range(10):
            board[r][c] += 1
            if board[r][c] > 9:
                flash.append((r, c))
    
    while flash:
        x, y = flash.pop()
        if (x, y) in flashed: continue
        board[x][y] += 1
        if board[x][y] > 9:
            flashed.add((x, y))

            dirs = [(i, j) for i in [-1,0,1] for j in [-1,0,1] if i or j]
            for i, j in dirs:
                if 0 <= x + i < 10 and 0 <= y + j < 10:
                    flash.append((x + i, y + j))
    
    for x, y in flashed:
        board[x][y] = 0
    
    mem[strung] = len(flashed), stringify(board)
    return len(flashed), board



time = 0
flash = 0
while flash < 100:
    flash, board = step(board)
    time += 1
print(time)

# for i in range(steps):
    