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

fold = int(folds[0][1])

points = set((i if i <= fold else 2 * fold - i,j) for i,j in points)
print(len(points))