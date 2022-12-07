"""
Tic Tac Toe Player

This file is AI for a Tic Tac Toe game
It geneates the best move based on a given board and
responds to the players moves
The AI is unbeatable

author: Navarre Frede
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

"""
Returns starting state of the board.
"""
def initial_state():

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

"""
Returns whose turn it is based on the given board
"""
def player(board):
    xnum = 0
    onum = 0
    for i in range(len(board)):
        for x in board[i]:
            if x == X:
                xnum += 1
            elif x == O:
                onum += 1
    if xnum <= onum:
        return X
    return O



"""
Returns all possible actions on a given board
returns an array of tuples containing the i and
j positions of the actions on the board
"""
def actions(board):
    answer = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                answer.append((i, j))
    return answer


"""
Returns the board that results from making move (i, j) on the board.
Throws an exception if the action spot on the board is not empty
"""

def result(board, action):
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Action is not valid for the given board. The spot is not empty")
        return None

    newboard = copy.deepcopy(board)
    newboard[action[0]][action[1]] = player(board)

    return newboard


"""
Returns the winner of the game, if there is one
Checks Rows, collumns and diagonals to see if O or X has won the game
Uses sets to remove duplicates and check if a row, collumn or 
diagonal is all X's or all O's
Returns the winner or None if there is no winner
"""
def winner(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != EMPTY:
            return row[0]
    for i in range(len(board[0])):
        column= [board[0][i], board[1][i], board[2][i]]
        if len(set(column)) == 1 and column[0] != EMPTY :
            return column[0]
    diagonals = [board[0][0], board[1][1], board[2][2]]
    if len(set(diagonals)) == 1 and diagonals[0] != EMPTY:
        return diagonals[0]
    diagonals = [board[0][2], board[1][1], board[2][0]]
    if len(set(diagonals)) == 1 and diagonals[0] != EMPTY:
        return diagonals[0]
    return None

"""
Returns True if game is over, False otherwise.
"""
def terminal(board):

    if winner(board) != None:
        return True
    # Checks if the games is still in progress
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                return False
    return True

"""
Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
"""
def utility(board):
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0

"""
Returns the optimal action for the current player on the board.
Returns None if the game is over
"""
def minimax(board):
    if terminal(board):
        return None

    if player(board) == X:
        moves = []
        # Creates a two-dimensional array that stores all the value
        # from resulting from the action and the action itself
        for x in actions(board):
            # Uses min_value because the player is X and the next
            # player, O, wants to minimize the value
            moves.append([min_value(result(board, x)), x])

        # Sorts the array in decending order and returns the highest
        # value's corresponding action
        return sorted(moves, key=lambda x: x[0], reverse=True)[0][1]
    else:
        moves = []
        # Creates a two-dimensional array that stores all the value
        # from resulting from the action and the action itself
        for x in actions(board):
            # Uses max_value because the player is O and the next
            # player, X, wants to Maximize the value
            moves.append([max_value(result(board, x)), x])
        # Sorts the array in acending order and returns the lowest
        # value's corresponding action
        return sorted(moves, key=lambda x: x[0])[0][1]
"""
Returns the maximum value that is possible from the given board 
and its corresponding actions
Calls min_value if game is not over
"""
def max_value(board):
    if terminal(board):
        return utility(board)
    b = -math.inf
    acts = actions(board)
    ans = []
    for x in actions(board):
       b = max(b, min_value(result(board, x)))
    return b

"""
Returns the minimum value that is possible from the given board 
and its corresponding actions
Calls max_value if game is not over
"""
def min_value(board):
    if terminal(board):
        return utility(board)
    s = math.inf
    for x in actions(board):
       s = min(s, max_value(result(board, x)))
    return s