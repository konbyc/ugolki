from old_board import Board


class Player:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def choose_move(self, board):
        return (2, 0), (1, 0)
        start_row = start_col = finish_row = finish_col = -1
        for row in board.cells:
            for cell in row:
                if cell.color == self.color:
                    start_col = cell.col
                    start_row = cell.row
                if cell.color == "empty":
                    finish_col = cell.col
                    finish_row = cell.row
        return (start_row, start_col), (finish_row, finish_col)
