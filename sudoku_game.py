from sudoku import *
from turtle_setup import *
from button import *


class SudokuGUI:
    def __init__(self):
        self.is_game_over = False
        self.is_menu_over = False
        self.is_difficulty = False
        self.is_welcome_screen_over = False
        self.is_grid_size_over = False
        self.is_mode_selection = False
        self.mode = 'human'
        self.difficulty = 'easy'
        self.n = 9
        self.srn = int(math.sqrt(self.n))
        self.curr_number = 'none'
        self.s = Sudoku(self.n, 0)
        self.unmodifiable_cells = []
        self.buttons = []

        for button in range(16):
            temp = Button(str(button + 1))
            self.buttons.append(temp)

    def update_unmodifiable_cells(self):
        self.unmodifiable_cells = []
        for row_no in range(self.n):
            for col_no in range(self.n):
                if self.s.board[row_no][col_no] != 0:
                    self.unmodifiable_cells.append([row_no, col_no])

    def draw_board(self):
        d = 50
        if self.n == 4:
            d = 113
        if self.n == 16:
            d = 30

        x_shift = -160
        pen.goto(-d * self.n // 2 + x_shift, d * self.n // 2)
        pen.setheading(0)
        pen.pendown()
        pen.pensize(5)
        for i in range(4):
            pen.forward(d * self.n)
            pen.right(90)
        pen.pensize(1)
        pen.penup()
        for i in range(self.n):
            if i == 0:
                continue
            pen.goto(-d * self.n // 2 + i * d + x_shift, d * self.n // 2)
            pen.setheading(270)
            pen.pendown()
            pen.forward(d * self.n)
            pen.penup()
        for i in range(self.n):
            if i == 0:
                continue
            pen.goto(-d * self.n // 2 + x_shift, d * self.n // 2 - i * d)
            pen.setheading(0)
            pen.pendown()
            pen.forward(d * self.n)
            pen.penup()
        pen.pensize(4)
        for i in range(0, self.n, int(math.sqrt(self.n))):
            if i == 0:
                continue
            pen.goto(-d * self.n // 2 + i * d + x_shift, d * self.n // 2)
            pen.setheading(270)
            pen.pendown()
            pen.forward(d * self.n)
            pen.penup()
        for i in range(0, self.n, int(math.sqrt(self.n))):
            if i == 0:
                continue
            pen.goto(-d * self.n // 2 + x_shift, d * self.n // 2 - i * d)
            pen.setheading(0)
            pen.pendown()
            pen.forward(d * self.n)
            pen.penup()
        screen.update()

    def draw_buttons(self):
        self.srn = int(math.sqrt(self.n))
        active_buttons = [i for i in self.buttons if self.buttons.index(i) < self.n]
        for i in self.buttons:
            i.is_active = False
        for i in active_buttons:
            i.is_active = True
            size = 25
            if self.n == 4:
                size = 30
            if self.n == 9:
                i.width = 75
                i.length = 75
            if self.n == 4:
                i.width = 100
                i.length = 100
            if self.n == 16:
                i.width = 60
                i.length = 60

            i.x = 150 + (self.buttons.index(i) % self.srn) * i.length
            if self.n == 4:
                i.y = 125 - (self.buttons.index(i) // self.srn) * i.width
            else:
                i.y = 150 - (self.buttons.index(i) // self.srn) * i.width
            pen.goto(i.x, i.y)
            pen.setheading(0)
            pen.pendown()
            for j in range(2):
                pen.forward(i.length)
                pen.left(90)
                pen.forward(i.width)
                pen.left(90)
            pen.penup()
            if int(i.message) < 10:
                pen.goto(i.x + i.length // 2 - size * 1 // 3, i.y + i.width // 2 - size * 3 // 4)
            else:
                pen.goto(i.x + i.length // 2 - size * 2 // 3, i.y + i.width // 2 - size * 3 // 4)
            pen.write(i.message, font=('Arial', size, 'normal'))
            if not i.is_active:
                pen.goto(i.x, i.y + i.width)
                pen.pendown()
                pen.goto(i.x + i.length, i.y)
                pen.penup()
            if i.is_selected:
                pen.goto(i.x + 5, i.y + i.width - 5)
                pen.pendown()
                for k in range(2):
                    pen.forward(i.length - 10)
                    pen.right(90)
                    pen.forward(i.width - 10)
                    pen.right(90)
                screen.update()
                pen.penup()

    def draw_numbers_on_grid(self):
        d = 50
        size = 25
        if self.n == 4:
            d = 113
            size = 50
        if self.n == 16:
            d = 30
            size = 14
        x_shift = -160
        for i in range(self.n):
            for j in range(self.n):
                if self.s.board[i][j] != 0:
                    if [i, j] in self.unmodifiable_cells:
                        pen2.setheading(0)
                        pen2.fillcolor('white')
                        pen2.color('#0099FF')
                    else:
                        pen2.pencolor('white')
                        num = self.s.board[i][j]
                        self.s.board[i][j] = 999
                        if self.s.isvalid(num, i, j):
                            pen2.pencolor('white')
                        else:
                            pen2.pencolor('red')
                        self.s.board[i][j] = num
                    if self.s.is_solved():
                        pen2.color('spring green')
                    if self.n == 4:
                        pen2.goto(-d * self.n // 2 + x_shift + j * d + 40, d * self.n // 2 - i * d - 90)
                    if self.n == 9:
                        pen2.goto(-d * self.n // 2 + x_shift + j * d + 15, d * self.n // 2 - i * d - 45)
                    if self.n == 16:
                        if self.s.board[i][j] >= 10:
                            pen2.goto(-d * self.n // 2 + x_shift + j * d + 5, d * self.n // 2 - i * d - 27)
                        else:
                            pen2.goto(-d * self.n // 2 + x_shift + j * d + 12, d * self.n // 2 - i * d - 27)
                    pen2.write(str(self.s.board[i][j]), font=('Arial', size, 'normal'))

    @staticmethod
    def rect(t, x, y):
        t.pendown()
        for i in range(2):
            t.forward(x)
            t.right(90)
            t.forward(y)
            t.right(90)
        t.penup()

    def welcome_screen(self):
        screen.setup(600, 600)
        pen.clear()
        pen2.clear()
        pen.goto(-210, 50)
        pen.write('SUDOKU', font=('Arial', 75, 'normal'))
        pen.goto(-95, -0)
        self.rect(pen, 200, 75)
        pen.goto(-95, -100)
        self.rect(pen, 200, 75)
        pen.goto(-50, -65)
        pen.write('PLAY', font=('Arial', 35, 'normal'))
        pen.goto(-50, -165)
        pen.write('QUIT', font=('Arial', 35, 'normal'))
        while True:
            screen.onclick(self.welcome_screen_check)
            if self.is_welcome_screen_over:
                return
            screen.update()
            time.sleep(0.01)

    def grid_size_screen(self):
        pen.clear()
        pen2.clear()
        screen.setup(600, 600)
        pen.goto(-100, 130)
        pen.write('SELECT', font=('Arial', 40, 'normal'))
        pen.goto(-110, 50)
        pen.write('VARIANT', font=('Arial', 40, 'normal'))
        pen.goto(-95, -0)
        self.rect(pen, 200, 50)
        pen.goto(-95, -75)
        self.rect(pen, 200, 50)
        pen.goto(-95, -150)
        self.rect(pen, 200, 50)
        pen.goto(-40, -50)
        pen.write('4 X 4', font=('Arial', 30, 'normal'))
        pen.goto(-40, -125)
        pen.write('9 X 9', font=('Arial', 30, 'normal'))
        pen.goto(-60, -200)
        pen.write('16 X 16', font=('Arial', 30, 'normal'))
        while True:
            screen.onclick(self.grid_size_check)
            if self.is_grid_size_over:
                return
            screen.update()
            time.sleep(0.01)

    def mode_selection_screen(self):
        pen.clear()
        pen2.clear()
        screen.setup(600, 600)
        pen.goto(-140, 75)
        pen.write('SELECT MODE', font=('Arial', 30, 'normal'))
        pen.goto(-170, 0)
        self.rect(pen, 100, 50)
        pen.goto(-70, 0)
        self.rect(pen, 270, 50)
        pen.goto(-156, -47)
        pen.write('You', font=('Arial', 30, 'normal'))
        pen.goto(-170, -75)
        self.rect(pen, 200, 50)
        pen.goto(30, -75)
        self.rect(pen, 170, 50)
        pen.goto(-156, -125)
        pen.write('Computer', font=('Arial', 30, 'normal'))
        pen.goto(-60, -22)
        pen.write('Solve a computer-generated', font=('Arial', 10, 'normal'))
        pen.goto(-60, -42)
        pen.write('puzzle', font=('Arial', 10, 'normal'))
        pen.goto(35, -98)
        pen.write('Find a solution to a puzzle', font=('Arial', 10, 'normal'))
        pen.goto(35, -118)
        pen.write('using the computer', font=('Arial', 10, 'normal'))
        while True:
            screen.onclick(self.mode_selection_screen_check)
            if self.is_mode_selection:
                return
            screen.update()
            time.sleep(0.01)

    def difficulty_screen(self):
        pen.clear()
        pen2.clear()
        screen.setup(600, 600)
        pen.goto(-100, 130)
        pen.write('SELECT', font=('Arial', 40, 'normal'))
        pen.goto(-150, 50)
        pen.write('DIFFICULTY', font=('Arial', 40, 'normal'))
        pen.goto(-95, -0)
        self.rect(pen, 200, 50)
        pen.goto(-95, -75)
        self.rect(pen, 200, 50)
        pen.goto(-95, -150)
        self.rect(pen, 200, 50)
        pen.goto(-45, -50)
        pen.write('EASY', font=('Arial', 30, 'normal'))
        pen.goto(-75, -125)
        pen.write('MEDIUM', font=('Arial', 30, 'normal'))
        pen.goto(-45, -200)
        pen.write('HARD', font=('Arial', 30, 'normal'))
        while True:
            screen.onclick(self.difficulty_check)
            if self.is_difficulty:
                return
            screen.update()
            time.sleep(0.01)

    def number_buttons_check(self, x, y):
        if self.buttons[0].x < x < self.buttons[self.srn - 1].x + self.buttons[self.srn - 1].length:
            if self.buttons[self.n - 1].y < y < self.buttons[0].y + self.buttons[0].width:
                for i in self.buttons:
                    if i.is_active:
                        if i.x < x < i.x + i.length:
                            if i.y < y < i.y + i.width:
                                for k in self.buttons:
                                    if k == i:
                                        continue
                                    k.is_selected = False
                                i.is_selected = not i.is_selected
                                if i.is_selected:
                                    self.curr_number = int(i.message)
                                else:
                                    self.curr_number = 'none'
                                pen.clear()
                                self.is_machine_check()
                                self.draw_board()
                                self.draw_buttons()

    def grid_check(self, x, y):
        d = 50
        if self.n == 4:
            d = 113
        if self.n == 16:
            d = 30

        x_shift = -160
        if -d * self.n // 2 + x_shift < x < d * self.n // 2 + x_shift:
            if -d * self.n // 2 < y < d * self.n // 2:
                c = int((x - (-d * self.n // 2 + x_shift)) // d)
                r = int(-(y - (d * self.n // 2)) // d)
                if [r, c] not in self.unmodifiable_cells:
                    if self.curr_number != 'none':
                        if self.s.board[r][c] == int(self.curr_number):
                            self.s.board[r][c] = 0
                        else:
                            self.s.board[r][c] = int(self.curr_number)
                        pen2.clear()
                        self.draw_numbers_on_grid()
                        screen.update()

    def check_buttons(self, x, y):
        self.number_buttons_check(x, y)
        self.grid_check(x, y)
        if 150 < x < 350:
            if -150 < y < -100:
                if self.mode == 'machine':
                    pen.goto(150, -75)
                    pen.write('Solving...', font=('Arial', 20, 'normal'))
                    if self.s.solve_board(0, 0):
                        pen.clear()
                        self.draw_buttons()
                        self.draw_board()
                        pen.goto(150, -75)
                        pen.write('Solved!', font=('Arial', 20, 'normal'))
                    else:
                        pen.clear()
                        self.draw_buttons()
                        self.draw_board()
                        pen.goto(150, -75)
                        pen.write('No Solution!', font=('Arial', 20, 'normal'))
                        if time.time() - self.s.timer > 120:
                            pen.goto(-250, -280)
                            pen.write('Reason : Solution took longer than time limit (60 seconds)',
                                      font=('Arial', 10, 'normal'))
                        else:
                            pen.goto(-250, -280)
                            pen.write(
                                'Reason : One or more numbers may not be possible to put in a location',
                                font=('Arial', 10, 'normal'))
                self.is_machine_check()
                self.draw_numbers_on_grid()
            if -225 < y < -175:
                self.is_game_over = True

    def is_machine_check(self):
        if self.mode == 'machine':
            pen.pensize(4)
            pen.goto(150, -100)
            self.rect(pen, 200, 50)
            pen.goto(200, -150)
            pen.write('Solve', font=('Arial', 30, 'normal'))
        pen.pensize(4)
        pen.goto(150, -175)
        self.rect(pen, 200, 50)
        pen.goto(175, -220)
        pen.write('Main Menu', font=('Arial', 25, 'normal'))

    def welcome_screen_check(self, x, y):
        if -95 < x < 105:
            if -75 < y < 0:
                self.is_welcome_screen_over = True
            elif -175 < y < -100:
                screen.bye()
                quit()

    def grid_size_check(self, x, y):
        if -95 < x < 105:
            if -50 < y < 0:
                self.is_grid_size_over = True
                self.n = 4
            elif -125 < y < -75:
                self.is_grid_size_over = True
                self.n = 9
            elif -200 < y < -150:
                self.is_grid_size_over = True
                self.n = 16
            self.srn = int(math.sqrt(self.n))

    def mode_selection_screen_check(self, x, y):
        if -150 < x < 220:
            if -50 < y < 0:
                self.is_mode_selection = True
                self.mode = 'human'
            if -125 < y < -75:
                self.is_mode_selection = True
                self.mode = 'machine'

    def difficulty_check(self, x, y):
        if -95 < x < 105:
            if -50 < y < 0:
                self.is_difficulty = True
                self.difficulty = 'easy'
            elif -125 < y < -75:
                self.is_difficulty = True
                self.difficulty = 'medium'
            elif -200 < y < -150:
                self.is_difficulty = True
                self.difficulty = 'hard'

    def play_game(self):
        m = 0
        screen.setup(900, 600)
        pen.clear()
        pen2.clear()
        if self.mode == 'human':
            if self.difficulty == 'easy':
                if self.n == 4:
                    m = 5
                elif self.n == 9:
                    m = self.n * 4
                else:
                    m = self.n * 6
            elif self.difficulty == 'medium':
                if self.n == 4:
                    m = 8
                elif self.n == 9:
                    m = self.n * 6
                else:
                    m = self.n * 8
            elif self.difficulty == 'hard':
                if self.n == 4:
                    m = 10
                elif self.n == 9:
                    m = self.n * 7 + 6
                else:
                    m = self.n * 10
            pen.goto(150, -200)
            pen.clear()
            pen.write('Generating Board...', font=('Arial', 15, 'normal'))
            self.s = Sudoku(self.n, m)
            self.s.board_generate()
            self.update_unmodifiable_cells()
            pen.clear()
            pen2.clear()
        else:
            self.s = Sudoku(self.n, 0)
            self.update_unmodifiable_cells()
        self.is_machine_check()
        self.draw_board()
        self.draw_buttons()
        self.draw_numbers_on_grid()
        while True:
            screen.onclick(self.check_buttons)
            if self.is_game_over:
                return
            screen.update()
            time.sleep(0.01)

    def run(self):
        while True:
            for button in self.buttons:
                button.is_selected = False
                button.is_active = False
            self.n = 9
            self.is_game_over = False
            pen.clear()
            pen2.clear()
            self.is_welcome_screen_over = False
            self.is_grid_size_over = False
            self.is_mode_selection = False
            self.is_difficulty = False
            self.welcome_screen()
            self.grid_size_screen()
            self.mode_selection_screen()
            if self.mode == 'human':
                self.difficulty_screen()
            self.play_game()
            time.sleep(0.01)
