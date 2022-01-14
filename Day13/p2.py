def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

inp = input('Day13/in.txt')

ind = 0

while inp[ind]:
    ind += 1
    
points, folds = set((int(j) for j in i.split(',')) for i in inp[:ind]), [i.split('=') for i in inp[ind + 1:]]

for ins, fold in folds:
    ins = ins[-1]
    fold = int(fold)
    points = set((2 * fold - i if ins == 'x' and i > fold else i,
                  2 * fold - j if ins == 'y' and j > fold else j)
                  for i,j in points)

for c in range(max(i[1] for i in points) + 1):
    for r in range(max(i[0] for i in points) + 1):
        print(' ▇'[(r,c) in points], end='')
    print()