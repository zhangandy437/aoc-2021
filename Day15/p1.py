def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return [[int(i) for i in l] for l in lines]

maze = input('Day15/in.txt')
maze[0][0] = 0

for r in range(len(maze)):
    for c in range(len(maze[0])):
        if r and c:
            maze[r][c] += min(maze[r - 1][c], maze[r][c - 1])
        elif r:
            maze[r][c] += maze[r - 1][c]
        elif c:
            maze[r][c] += maze[r][c - 1]
        
print(maze[-1][-1])