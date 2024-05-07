import random, turtle
from board import Board, STARTING_POSITIONS, make_human_readable

n = 0


def start_game():
    board.draw_board()
    screen.update()
    turn()
    screen.onkeypress(turn, "space")


def turn():
    global n
    board.valid_moves = []

    if n > 99:
        with open('./games/game.txt', 'w') as game:
            game.write(make_human_readable(moves_history))
            # game.write(str(moves_history))
        return

    if n % 2 == 0:
        for piece in board.white:
            board.valid_moves.extend(board.get_valid_moves(piece))

        move = random.choice(board.valid_moves)
        board.white[board.white.index(move[0])] = move[1]
    else:
        for piece in board.black:
            board.valid_moves.extend(board.get_valid_moves(piece))

        move = random.choice(board.valid_moves)
        board.black[board.black.index(move[0])] = move[1]

    n += 1
    moves_history.append(move)
    print(make_human_readable([move]).strip())

    screen.update()
    board.clear()
    board.draw_board()


screen = turtle.Screen()
screen.setup(430, 310)
screen.colormode(255)
screen.bgcolor(217, 179, 140)
screen.title("ugolki")
screen.tracer(0)

board = Board(STARTING_POSITIONS[0], STARTING_POSITIONS[1])
board.draw_board()
moves_history = []

screen.update()
screen.onkeypress(screen.bye, "Escape")
screen.onkeypress(start_game, "space")
screen.listen()
screen.exitonclick()
