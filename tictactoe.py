"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
SIZE_OF_GAME = 9


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
    x, o = 0, 0
    for j in range(len(board)):
        for i in board[j]:
            if i == X:
                x += 1
            elif i == O:
                o += 1
    if x > o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                e = (i,j)
                actions_set.add(e)
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]
    board_copy = copy.deepcopy(board)
    if board[i][j] == EMPTY:
        board_copy[i][j] = player(board)
        return board_copy
    else:
        raise ValueError
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    z = len(board)
    for row in board:
        if row.count(X) == z: return X
        elif row.count(O) == z: return O

    for j in range(z):
        column = [board[i][j] for i in range(z)]
        if column.count(X) == z: return X
        elif column.count(O) == z: return O
    
    diagonalA = [board[e][e] for e in range(z)]
    if diagonalA.count(X) == z: return X
    if diagonalA.count(O) == z: return O

    diagonalB = [board[i][j] for i, j in zip(reversed(range(z)),range(len(board[0])))]
    if diagonalB.count(X) == z: return X
    if diagonalB.count(O) == z: return O
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    else:
        x, o = 0, 0 
        for row in board:
            x += row.count(X)
            o += row.count(O)
        if (x + o) == SIZE_OF_GAME:
            return True
        else:
            return False
    
    
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X: return 1
    elif win == O: return -1
    else: return 0
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    Recursive algo, plays for both sides.
    MAX_VALUE, MIN_VALUE, math.inf
    Get the current playe
    X is maximazing
    O is minimazing
    """
    ALPHA = -math.inf
    BETA = math.inf

    def max_value(board,ALPHA,BETA):
        if terminal(board):
            return utility(board)
        
        v = -math.inf

        for action in actions(board):
            new_board= result(board, action)
            v = max(v, min_value(new_board,ALPHA,BETA))
            ALPHA = max(ALPHA,v)
            if BETA <= ALPHA:
                break
        return v

    def min_value(board,ALPHA,BETA):
        if terminal(board):
            return utility(board)
        
        v = math.inf
        
        for action in actions(board):
            new_board= result(board, action)
            v = min(v, max_value(new_board,ALPHA,BETA))
            BETA = min(BETA, v)
            if BETA <= ALPHA:
                break
        return v

    if terminal(board):
        value = utility(board)
        return None

    pla = player(board)
    if pla == X:
        moves = []
        
        for action in actions(board):
            new_board = result(board,action)
            value = min_value(new_board,ALPHA,BETA)
            move = {'value': value, 'action': action}
            moves.append(move)
       
        max_move = max(moves, key=lambda move:move['value'])
        return max_move['action']

    elif pla == O:
        moves = []
        
        for action in actions(board):
            new_board = result(board,action)
            value = max_value(new_board,ALPHA,BETA)
            move = {'value': value, 'action': action}
            moves.append(move)

        min_move = min(moves, key=lambda move:move['value'])
        return min_move['action']    
