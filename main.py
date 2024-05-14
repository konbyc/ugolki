import random, turtle
from board import Board, human_readable, STARTING_POSITIONS
import strategy

already_playing = False


def start_game():
    global already_playing
    if already_playing:
        return
    already_playing = True
    turn()


def turn():
    if board.game_over:
        return
    board.generate_moves()
    move = strategy.choose_move(board)
    board.make_move(move)
    board.last_move = move
    board.turn_number += 1
    moves_history.append(move)
    board.check_win()
    board.clear()
    board.draw_board()
    screen.update()
    screen.onkeypress(turn, "space")


screen = turtle.Screen()
screen.setup(550, 550)
screen.colormode(255)
screen.bgcolor(217, 179, 140)
screen.title("ugolki")
screen.tracer(0)

board = Board(STARTING_POSITIONS[0], STARTING_POSITIONS[1])
board.draw_board()
moves_history = []

screen.onkeypress(screen.bye, "Escape")
screen.onkeypress(start_game, "space")
screen.listen()
screen.exitonclick()

with open('./games/game.txt', 'w') as game:
    game.write(human_readable(moves_history))
    # game.write(str(moves_history))