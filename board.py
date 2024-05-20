from turtle import Turtle

SQUARE = 60
SQ_HOR = 8
SQ_VER = 8

# [row, column]

STARTING_POSITIONS = [
    [[0, 0], [0, 1], [0, 2],
     [1, 0], [1, 1], [1, 2],
     [2, 0], [2, 1], [2, 2]],
    [[SQ_VER - 3, SQ_HOR - 3], [SQ_VER - 3, SQ_HOR - 2], [SQ_VER - 3, SQ_HOR - 1],
     [SQ_VER - 2, SQ_HOR - 3], [SQ_VER - 2, SQ_HOR - 2], [SQ_VER - 2, SQ_HOR - 1],
     [SQ_VER - 1, SQ_HOR - 3], [SQ_VER - 1, SQ_HOR - 2], [SQ_VER - 1, SQ_HOR - 1]]
]

# STARTING_POSITIONS = [
#     [[0, 0], [0, 1],
#      [1, 0], [1, 1]],
#     [[SQ_VER - 2, SQ_HOR - 2], [SQ_VER - 2, SQ_HOR - 1],
#      [SQ_VER - 1, SQ_HOR - 2], [SQ_VER - 1, SQ_HOR - 1]]
# ]

# STARTING_POSITIONS = [
#     [[0,0]],
#     [[1,0], [2,1], [2,3], [3,4], [4,3], [3,2]]
# ]

WIDTH = SQUARE * SQ_HOR
HEIGHT = SQUARE * SQ_VER

BOX_LEFT = -WIDTH / 2
BOX_RIGHT = WIDTH / 2
BOX_UP = HEIGHT / 2
BOX_DOWN = -HEIGHT / 2


def within_board(cell):
    if 0 <= cell[0] < SQ_VER and 0 <= cell[1] < SQ_HOR:
        return True
    else:
        return False


def human_readable(moves):
    writeup = ''
    for move in moves:
        start = Board.ALPHABET[move[0][1]] + str(move[0][0] + 1)
        finish = Board.ALPHABET[move[1][1]] + str(move[1][0] + 1)
        writeup += start + ':' + finish + '\n'
    return writeup


class Board(Turtle):

    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, white_starting_positions, black_starting_positions):
        super().__init__()
        self.white = white_starting_positions.copy()
        self.black = black_starting_positions.copy()
        self.turn_number = 0
        self.valid_moves = []
        self.last_move = []
        self.white_last_move = -10
        self.white_in_house = False
        self.black_in_house = False
        self.game_over = False

    def make_move(self, move):
        if self.turn_number % 2 == 0:
            self.white[self.white.index(move[0])] = move[1]
        else:
            self.black[self.black.index(move[0])] = move[1]

    def undo_move(self, move):
        if self.turn_number % 2 == 0:
            self.white[self.white.index(move[1])] = move[0]
        else:
            self.black[self.black.index(move[1])] = move[0]

    def draw_board(self):

        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color(153, 102, 51)

        for square_number in range(SQ_HOR + 1):  # draw cells
            self.goto(BOX_LEFT + SQUARE * square_number, BOX_UP)
            self.pendown()
            self.goto(BOX_LEFT + SQUARE * square_number, BOX_DOWN)
            self.penup()

        for square_number in range(SQ_VER + 1):
            self.goto(BOX_LEFT, BOX_UP - SQUARE * square_number)
            self.pendown()
            self.goto(BOX_RIGHT, BOX_UP - SQUARE * square_number)
            self.penup()

        for square_number in range(SQ_HOR):  # row and column numbering
            self.goto(BOX_LEFT + SQUARE * square_number + SQUARE / 2 - 3, BOX_DOWN - 20)
            self.color('black')
            self.write(Board.ALPHABET[square_number], font=('Arial', 12, 'normal'))

        for square_number in range(SQ_VER):
            self.goto(BOX_LEFT - 20, BOX_DOWN + SQUARE * square_number + SQUARE / 2 - 9)
            self.color('black')
            self.write(square_number + 1, font=('Arial', 11, 'normal'))

        for piece in self.white + self.black:  # draw pieces
            self.goto(BOX_LEFT + SQUARE * (piece[1] + 1 / 2), BOX_DOWN + SQUARE * (piece[0] + 1 / 2) - 20)
            if piece in self.white:
                self.color('white')
            else:
                self.color('black')
            self.pendown()
            self.begin_fill()
            self.circle(20, steps=6)
            self.end_fill()
            self.penup()

        if self.last_move:  # highlight last move
            fr = self.last_move[0]
            to = self.last_move[1]
            self.color(128, 229, 255)
            self.goto(BOX_LEFT + SQUARE * fr[1], BOX_DOWN + SQUARE * fr[0])
            self.pendown()
            self.goto(BOX_LEFT + SQUARE * (fr[1] + 1), BOX_DOWN + SQUARE * fr[0])
            self.goto(BOX_LEFT + SQUARE * (fr[1] + 1), BOX_DOWN + SQUARE * (fr[0] + 1))
            self.goto(BOX_LEFT + SQUARE * fr[1], BOX_DOWN + SQUARE * (fr[0] + 1))
            self.goto(BOX_LEFT + SQUARE * fr[1], BOX_DOWN + SQUARE * fr[0])
            self.penup()
            self.goto(BOX_LEFT + SQUARE * to[1], BOX_DOWN + SQUARE * to[0])
            self.pendown()
            self.goto(BOX_LEFT + SQUARE * (to[1] + 1), BOX_DOWN + SQUARE * to[0])
            self.goto(BOX_LEFT + SQUARE * (to[1] + 1), BOX_DOWN + SQUARE * (to[0] + 1))
            self.goto(BOX_LEFT + SQUARE * to[1], BOX_DOWN + SQUARE * (to[0] + 1))
            self.goto(BOX_LEFT + SQUARE * to[1], BOX_DOWN + SQUARE * to[0])
            self.penup()

    def free_cell(self, cell):
        if cell not in self.white + self.black:
            return True
        else:
            return False

    def get_valid_moves(self, start):

        def up(somewhere):
            return [somewhere[0] + 1, somewhere[1]]

        def down(somewhere):
            return [somewhere[0] - 1, somewhere[1]]

        def left(somewhere):
            return [somewhere[0], somewhere[1] - 1]

        def right(somewhere):
            return [somewhere[0], somewhere[1] + 1]

        def jump_up(somewhere):
            return [somewhere[0] + 2, somewhere[1]]

        def jump_down(somewhere):
            return [somewhere[0] - 2, somewhere[1]]

        def jump_left(somewhere):
            return [somewhere[0], somewhere[1] - 2]

        def jump_right(somewhere):
            return [somewhere[0], somewhere[1] + 2]

        def get_valid_steps(somewhere):
            steps = []
            if within_board(up(somewhere)) and self.free_cell(up(somewhere)):
                steps.append(up(somewhere))
            if within_board(down(somewhere)) and self.free_cell(down(somewhere)):
                steps.append(down(somewhere))
            if within_board(left(somewhere)) and self.free_cell(left(somewhere)):
                steps.append(left(somewhere))
            if within_board(right(somewhere)) and self.free_cell(right(somewhere)):
                steps.append(right(somewhere))
            return steps

        def get_valid_jumps(somewhere):

            landings = []

            if within_board(jump_up(somewhere)) and self.free_cell(jump_up(somewhere)) and not self.free_cell(
                    up(somewhere)):
                landings.append(jump_up(somewhere))
            if within_board(jump_down(somewhere)) and self.free_cell(jump_down(somewhere)) and not self.free_cell(
                    down(somewhere)):
                landings.append(jump_down(somewhere))
            if within_board(jump_left(somewhere)) and self.free_cell(jump_left(somewhere)) and not self.free_cell(
                    left(somewhere)):
                landings.append(jump_left(somewhere))
            if within_board(jump_right(somewhere)) and self.free_cell(jump_right(somewhere)) and not self.free_cell(
                    right(somewhere)):
                landings.append(jump_right(somewhere))

            return landings

        moves = []  # moves can be steps and jumps
        steps = get_valid_steps(start)
        jumps = get_valid_jumps(start)
        all_jumps = jumps

        while jumps:
            next_jumps = []
            for jump in jumps:
                for next_jump in get_valid_jumps(jump):
                    if next_jump not in jumps + next_jumps + all_jumps:
                        next_jumps.append(next_jump)
            all_jumps.extend(next_jumps)
            jumps = next_jumps

        for finish in steps + all_jumps:
            moves.append([start, finish])

        return moves

    def generate_moves(self):
        self.valid_moves = []
        if self.turn_number % 2 == 0:
            for piece in self.white:
                self.valid_moves.extend(self.get_valid_moves(piece))
        else:
            for piece in self.black:
                self.valid_moves.extend(self.get_valid_moves(piece))

    def check_win(self):
        if set(map(tuple, self.white)) - set(map(tuple, STARTING_POSITIONS[1])) == set():
            """Check that all white pieces have arrived in house"""
            if not self.white_in_house:
                self.white_last_move = self.turn_number
            self.white_in_house = True
        if set(map(tuple, self.black)) - set(map(tuple, STARTING_POSITIONS[0])) == set():
            """Check that all black pieces have arrived in house"""
            self.black_in_house = True
            if not self.white_in_house:
                self.game_over = True
                print('Black win')
        if self.turn_number == self.white_last_move + 1:
            if self.black_in_house:
                """If black finish one turn after white, then it's a draw"""
                self.game_over = True
                print('Draw')
            else:
                self.game_over = True
                print('White win')
