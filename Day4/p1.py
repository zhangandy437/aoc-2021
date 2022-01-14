def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

inp = input("/Users/andyzhang/Documents/sandbox/python/adventofcode2021/Day4/in.txt")
moves = [int(num) for num in inp[0].split(',')]

class Board:
    def __init__(self, arr):
        self.board = {int(num):(x,y) for x, row in enumerate(arr) for y, num in enumerate(row.split())}
        self.allnums = set(num for num in self.board.keys())
        self.rows = [0] * 5
        self.cols = [0] * 5
    
    def check_num(self, num):
        if num not in self.board: return False
        x, y = self.board[num]
        self.rows[x] += 1
        self.cols[y] += 1
        self.allnums.remove(num)
        return self.check_bingo()
        
    def check_bingo(self):
        return 5 [self.rows, self.cols]
    
    def get_unmarked(self):
        return sum(self.allnums)
        
        

boards = []
for i in range(2, len(inp) - 4, 6):
    boards.append(Board(inp[i:i+6]))
found = False
for move in moves:
    if not found:
        for board in boards:
            if board.check_num(move):
                un = board.get_unmarked()
                print(un, move, un * move)
                found = True