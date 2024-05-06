from turtle import Turtle


SQUARE = 60
SQ_HOR = 3
SQ_VER = 3
STARTING_PIECES = [
                    ["empty", "black", "black"],
                    ["empty", "empty", "black"],
                    ["white", "empty", "empty"],
                    ["white", "white", "empty"],
                  ]


WIDTH = SQUARE * SQ_HOR
HEIGHT = SQUARE * SQ_VER

BOX_LEFT = -WIDTH/2
BOX_RIGHT = WIDTH/2
BOX_UP = HEIGHT/2
BOX_DOWN = -HEIGHT/2


class Cell:

    def __init__(self, col_index, row_index, piece_color):
        self.col = col_index
        self.row = row_index
        self.color = piece_color
        self.selected = False


class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.cells = []
        self.penup()
        self.hideturtle()
        self.color(153, 102, 51)
        self.speed("fastest")
        for row in range(SQ_VER):
            self.cells.append([])
            for column in range(SQ_HOR):
                self.cells[row].append(Cell(col_index=column, row_index=row, piece_color=STARTING_PIECES[row][column]))
        self.draw_board()

    def draw_board(self):
        self.color(153, 102, 51)
        for square_number in range(SQ_HOR + 1):
            self.goto(BOX_LEFT + SQUARE * square_number, BOX_UP)
            self.pendown()
            self.goto(BOX_LEFT + SQUARE * square_number, BOX_DOWN)
            self.penup()
        for square_number in range(SQ_VER + 1):
            self.goto(BOX_LEFT, BOX_UP - SQUARE * square_number)
            self.pendown()
            self.goto(BOX_RIGHT, BOX_UP - SQUARE * square_number)
            self.penup()
        for row in self.cells:
            for cell in row:
                if cell.color != "empty":  # draw a piece
                    self.color(cell.color, cell.color)
                    self.goto(BOX_LEFT + SQUARE * (cell.col + 1/2), BOX_UP - SQUARE * (cell.row + 1/2) - 20)
                    self.pendown()
                    self.begin_fill()
                    self.circle(20, steps=6)
                    self.end_fill()
                    self.penup()
                if cell.selected:  # draw frame
                    self.color(128, 229, 255)
                    self.goto(BOX_LEFT + SQUARE * cell.col, BOX_UP - SQUARE * cell.row)
                    self.pendown()
                    self.goto(BOX_LEFT + SQUARE * (cell.col + 1), BOX_UP - SQUARE * cell.row)
                    self.goto(BOX_LEFT + SQUARE * (cell.col + 1), BOX_UP - SQUARE * (cell.row + 1))
                    self.goto(BOX_LEFT + SQUARE * cell.col, BOX_UP - SQUARE * (cell.row + 1))
                    self.goto(BOX_LEFT + SQUARE * cell.col, BOX_UP - SQUARE * cell.row)
                    self.penup()

    def make_move(self, move):
        start_cell = self.cells[move[0][0]][move[0][1]]
        finish_cell = self.cells[move[1][0]][move[1][1]]
        temp_color = start_cell.color
        start_cell.color = finish_cell.color
        finish_cell.color = temp_color
        self.draw_board()

    def select_cell(self, click_x, click_y):
        if not (BOX_LEFT < click_x < BOX_RIGHT and BOX_DOWN < click_y < BOX_UP):
            return
        col_index = int((click_x - BOX_LEFT) // SQUARE)
        row_index = int((BOX_UP - click_y) // SQUARE)
        for row in self.cells:
            for cell in row:
                if cell.selected and not (cell.col == col_index and cell.row == row_index):
                    cell.selected = not cell.selected
                    temp_color = cell.color
                    cell.color = self.cells[row_index][col_index].color
                    self.cells[row_index][col_index].color = temp_color
                    self.clear()
                    self.cells[row_index][col_index].selected = not self.cells[row_index][col_index].selected
        self.cells[row_index][col_index].selected = not self.cells[row_index][col_index].selected
        self.draw_board()
