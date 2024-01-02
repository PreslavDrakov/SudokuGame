from libraries import *
from turtle_setup import *


class Sudoku:
    def __init__(self, n=9, missing=0, demo=True):
        self.n = n
        self.board = [[0 for i in range(n)] for j in range(n)]
        self.unsolved_board = []
        self.srn = int(math.sqrt(n))
        self.missing = missing
        self.demo = demo
        self.timer = time.time()

    def fill_box(self, row, col):
        num = [i for i in range(1, self.n + 1)]
        for i in range(self.srn):
            for j in range(self.srn):
                x = random.choice(num)
                num.remove(x)
                self.board[row + i][col + j] = x

    def diagonal(self):
        for i in range(0, self.n, self.srn):
            self.fill_box(i, i)

    def is_used_in_row(self, n, r):
        for i in range(self.n):
            if self.board[r][i] == n:
                return True
        return False

    def is_used_in_column(self, n, c):
        for i in range(self.n):
            if self.board[i][c] == n:
                return True
        return False

    def is_used_in_box(self, n, r, c):
        box_r = self.srn * (r // self.srn)
        box_c = self.srn * (c // self.srn)
        for i in range(self.srn):
            for j in range(self.srn):
                if self.board[box_r + i][box_c + j] == n:
                    return True
        return False

    def isvalid(self, k, i, j):
        if not self.is_used_in_row(k, i):
            if not self.is_used_in_column(k, j):
                if not self.is_used_in_box(k, i, j):
                    return True
        return False

    def solve_board(self, row, col):
        r = row
        c = col
        screen.update()
        for i in range(self.n):
            for j in range(self.n):
                num = self.board[i][j]
                self.board[i][j] = 999
                if not self.isvalid(num, i, j) and num != 0:
                    self.board[i][j] = num
                    return False
                self.board[i][j] = num
        if r == self.n - 1 and c == self.n:
            return True
        if time.time() - self.timer > 60:
            return False
        if c == self.n:
            c -= c
            r += 1
        if self.board[r][c] != 0:
            return self.solve_board(r, c + 1)
        for i in range(1, self.n + 1):
            if self.isvalid(i, r, c):
                self.board[r][c] = i
                if self.demo:
                    os.system('CLS')
                    self.show_board()
                    response = input('Press Enter to see next stage ({skip} to skip preview) : ')
                    if response == 'skip':
                        self.demo = False
                if self.solve_board(r, c + 1):
                    return True
            self.board[r][c] = 0
        return False

    def remove_elements(self):
        already_removed = []
        count = 0
        while count < self.missing:
            r = random.randint(0, self.n - 1)
            c = random.randint(0, self.n - 1)
            if [r, c] not in already_removed:
                self.board[r][c] = 0
                count += 1
            already_removed.append([r, c])

    def board_generate(self):
        while True:
            for i in range(self.n):
                for j in range(self.n):
                    self.board[i][j] = 0
            self.diagonal()
            if self.solve_board(0, self.srn):
                break
        self.remove_elements()

    def show_board(self):
        t = '*' + '─' * (2 * self.srn + 1)
        print(t * self.srn + '*')
        for i in range(self.n):
            for j in range(self.n):
                if j % self.srn == 0:
                    print('│', end=' ')
                if self.board[i][j] != 0:
                    print(self.board[i][j], end=' ')
                else:
                    print('-', end=' ')
                if j == self.n - 1:
                    print('│', end=' ')
            print('')
            if (i + 1) % self.srn == 0:
                t = '*' + '─' * (2 * self.srn + 1)
                print(t * self.srn + '*')
