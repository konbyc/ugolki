from board import Board, STARTING_POSITIONS

board = Board(STARTING_POSITIONS[0], STARTING_POSITIONS[1])

for piece in board.white:
    board.possible_moves.extend(board.get_possible_moves(piece))

print(board.get_possible_moves([1, 2]))
