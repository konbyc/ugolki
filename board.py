SQ_HOR = 4
SQ_VER = 4

# [row, column]
STARTING_POSITIONS = [
    [[0, 0], [0, 1],
     [1, 0], [1, 1]],
    [[SQ_VER - 2, SQ_HOR - 2], [SQ_VER - 2, SQ_HOR - 1],
     [SQ_VER - 1, SQ_HOR - 2], [SQ_VER - 1, SQ_HOR - 1]]
]


def within_board(cell):
    if 0 <= cell[0] < SQ_VER and 0 <= cell[1] < SQ_HOR:
        return True
    else:
        return False


class Board:

    def __init__(self, white_starting_positions, black_starting_positions):
        self.white = white_starting_positions
        self.black = black_starting_positions
        self.possible_moves = []

    def free_cell(self, cell):
        if cell not in self.white + self.black:
            return True
        else:
            return False

    def get_possible_moves(self, piece):

        moves = []

        move_up = [piece[0] + 1, piece[1]]
        move_down = [piece[0] - 1, piece[1]]
        move_left = [piece[0], piece[1] - 1]
        move_right = [piece[0], piece[1] + 1]
        jump_up = [piece[0] + 2, piece[1]]
        jump_down = [piece[0] - 2, piece[1]]
        jump_left = [piece[0], piece[1] - 2]
        jump_right = [piece[0], piece[1] + 2]

        if within_board(move_up) and self.free_cell(move_up):
            moves.append([piece, move_up])
        if within_board(move_down) and self.free_cell(move_down):
            moves.append([piece, move_down])
        if within_board(move_left) and self.free_cell(move_left):
            moves.append([piece, move_left])
        if within_board(move_right) and self.free_cell(move_right):
            moves.append([piece, move_right])

        if within_board(jump_up) and self.free_cell(jump_up) and not self.free_cell(move_up):
            moves.append([piece, jump_up])
        if within_board(jump_down) and self.free_cell(jump_down) and not self.free_cell(move_down):
            moves.append([piece, jump_down])
        if within_board(jump_left) and self.free_cell(jump_left) and not self.free_cell(move_left):
            moves.append([piece, jump_left])
        if within_board(jump_right) and self.free_cell(jump_right) and not self.free_cell(move_right):
            moves.append([piece, jump_right])

        return moves

