import random
from board import SQ_HOR, SQ_VER, STARTING_POSITIONS


def distance(x, y):
    return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** (1 / 2)


# def distance(piece, board):
#     if piece in board.white:
#         free_cells_remaining = set(map(tuple, STARTING_POSITIONS[1])).difference(set(map(tuple, board.white)))
#         locus = random.choice(list(free_cells_remaining))
#         return ((locus[1] - piece[1])**2 + (locus[0] - piece[0])**2)**(1/2)
#         # return ((SQ_HOR - 1 - piece[1])**2 + (SQ_VER - 1 - piece[0])**2)**(1/2)
#     if piece in board.black:
#         free_cells_remaining = set(map(tuple, STARTING_POSITIONS[0])).difference(set(map(tuple, board.black)))
#         locus = random.choice(list(free_cells_remaining))
#         return ((locus[1] - piece[1])**2 + (locus[0] - piece[0])**2)**(1/2)
#         # return (piece[1]**2 + piece[0]**2)**(1/2)
#

def distance_aggregate(board):
    dist = 0
    if board.turn_number % 2 == 0:
        goal = [SQ_HOR - 1, SQ_VER - 1]
        for piece in board.white:
            dist += distance(piece, goal)
    else:
        goal = [0, 0]
        for piece in board.black:
            dist += distance(piece, goal)
    return dist


def choose_move(board):
    dist = dict()
    for move in board.valid_moves:
        board.make_move(move)
        dist[tuple(map(tuple, move))] = distance_aggregate(board)
        board.undo_move(move)
    choice = min(dist, key=dist.get)
    return list(map(list, choice))
