import tictactoe as ttt

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [O, EMPTY, X]]

board= initial_state()

print(board)


actions = ttt.actions(board)
print(actions)
for action in actions:
    new_board = ttt.result(board,action)
    print("New board: ", new_board)

new_board = ttt.result(board,(2,0))
print("New board: ", new_board)
# print(board[0])
# z = len(board)
# diagonalB = [board[i][j] for i, j in zip(reversed(range(z)),range(len(board[0])))]

print("WINNER: ", ttt.winner(board))

# print("diB: ", diagonalB)
print("Terminal: ", ttt.terminal(board))
print("Utility: ", ttt.utility(board))
print(board[2][1])
print("\nCALL MINIMAX")

# print("max_value: ", ttt.max_value(board))
# print()
# print("min_value", ttt.min_value(board))
print("Minimax: ", ttt.minimax(board))

