"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count<= o_count else O
    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_movies = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_movies.add((i,j))
    return possible_movies
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #raise NotImplementedError
    i, j = action
    if board[i][j] != EMPTY:
        raise Exception("Invalid move")
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #raise NotImplementedError
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if all(cell==X for cell in board[i]):
            return X
        if all(row[i] == X for row in board):
            return X
    if all(board[i][i] == X for i in range(3)) or all(board[i][2-i] == X for i in range(3)):
        return X
    
    for i in range(3):
        if all(cell== O for cell in board[i]):
            return O
        if all(row[i] == O for row in board):
            return O
    if all(board[i][i] == O for i in range(3)) or all(board[i][2-i]== O for i in range(3)):
        return O
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) or all(all(cell is not None for cell in row) for row in board)
    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #raise NotImplementedError
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #raise NotImplementedError
    if terminal(board):
        return None
    
    if player(board) == X:
        max_utility = -float('inf')
        best_action = None
        for action in actions(board):
            new_utility = min_value(result(board, action))
            if new_utility > max_utility:
                max_utility = new_utility
                best_action = action
        return best_action
    else:
        min_utility = float('inf')
        best_action = None
        for action in actions(board):
            new_utility = max_value(result(board, action))
            if new_utility < min_utility:
                min_utility = new_utility
                best_action = action
        return best_action

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -float('inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


