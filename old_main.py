import turtle
from old_board import Board
from old_player import Player
from old_game import Game


screen = turtle.Screen()
screen.setup(430, 310)
screen.colormode(255)
screen.bgcolor(217, 179, 140)
screen.title("ugolki")
screen.tracer(0)

board = Board()
alice = Player("Alice", "white")
bob = Player("Bob", "black")
game = Game()

current_player = 1
while game.continues:
    if current_player == 1:
        move = alice.choose_move(board)
    else:
        move = bob.choose_move(board)
    board.make_move(move)
    current_player *= -1
    game.continues = False

turtle.onscreenclick(board.select_cell)

screen.update()
screen.listen()
screen.onkeypress(screen.bye, "Escape")
turtle.mainloop()
