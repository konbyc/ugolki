import random
from board import SQ_HOR, SQ_VER, STARTING_POSITIONS, human_readable


def distance(x, y):
    return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** (1 / 2)


def distance_aggregate(board, to_where):
    dist = 0
    if board.turn_number % 2 == 0:
        for piece in board.white:
            dist += distance(piece, to_where)
    else:
        for piece in board.black:
            dist += distance(piece, to_where)
    return dist


def goal(board, piece):
    if board.turn_number % 2 == 0:
        if piece in STARTING_POSITIONS[1]:
            return [SQ_HOR - 1, SQ_VER - 1]
        remaining_slots = list(set(map(tuple, STARTING_POSITIONS[1])) - set(map(tuple, board.white)))
    else:
        if piece in STARTING_POSITIONS[0]:
            return [0, 0]
        remaining_slots = list(set(map(tuple, STARTING_POSITIONS[0])) - set(map(tuple, board.black)))
    if remaining_slots:
        return random.choice(remaining_slots)
    return


def choose_move(board):
    dist = dict()
    for move in board.valid_moves:
        board.make_move(move)
        dist[tuple(map(tuple, move))] = distance_aggregate(board, goal(board, move[0]))
        board.undo_move(move)
    choice = min(dist, key=dist.get)
    return list(map(list, choice))
