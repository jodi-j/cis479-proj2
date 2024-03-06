"""
Tic Tac Toe Player
"""

import math
import copy

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
    
    The player function should take a board state as input, and return which player’s turn it is
    (either X or O).
    o In the initial game state, X gets the first move. Subsequently, the player alternates with
    each additional move.
    o Any return value is acceptable if a terminal board is provided as input (i.e., the game is
    already over)
    """
    tempX = 0
    tempO = 0
    currPlayer = X
    for row in board:
        for col in row:
            if(col == 'X'):
                tempX += 1
            elif(col == 'O'):
                tempO += 1
    
    if(board == initial_state()):
        currPlayer = X
    elif(tempX < tempO):
        currPlayer = X
    elif(tempX > tempO):
        currPlayer = O
    
    return currPlayer
    
    raise NotImplementedError

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    
    The actions function should return a set of all of the possible actions that can be taken on a
    given board.
    o Each action should be represented as a tuple (i, j) where i corresponds to the row of the
    move (0, 1, or 2) and j corresponds to which cell in the row corresponds to the move
    (also 0, 1, or 2).
    o Possible moves are any cells on the board that do not already have an X or an O in them.
    o Any return value is acceptable if a terminal board is provided as input.
    """
    
    emptySpots = []
    for row, sublist in enumerate(board):
        for column, item in enumerate(sublist):
            if item == EMPTY:
                emptySpots.append((row, column))
    
    return emptySpots
    
    raise NotImplementedError

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    
    The result function takes a board and an action as input, and should return a new board state,
    without modifying the original board.
    o If action is not a valid action for the board, your program should raise an exception.
    o The returned board state should be the board that would result from taking the original
    input board, and letting the player whose turn it is make their move at the cell indicated
    by the input action.
    o Importantly, the original board should be left unmodified: since Minimax will ultimately
    require considering many different board states during its computation. This means that
    simply updating a cell in board itself is not a correct implementation of the result
    function. You’ll likely want to make a deep copy of the board first before making any
    changes.
    """

    newBoard = copy.deepcopy(board)
    row, col = action
    if(newBoard[row][col] == EMPTY):
        newBoard[row][col] = player(newBoard)
    elif(newBoard[row][col] != EMPTY): 
        print("WRONG") #TO DO: raise specific error for pygame visually
    
    
    for row in newBoard:
        print(row)
    
    return newBoard
    raise NotImplementedError

def winner(board):
    """
    Returns the winner of the game, if there is one.
    
    The winner function should accept a board as input and return the winner of the board if there
    is one.
    o If the X player has won the game, your function should return X. If the O player has won
    the game, your function should return O.
    o One can win the game with three of their moves in a row horizontally, vertically, or
    diagonally.
    o You may assume that there will be at most one winner (that is, no board will ever have
    both players with three-in-a-row, since that would be an invalid board state).
    o If there is no winner of the game (either because the game is in progress, or because it
    ended in a tie), the function should return None.
    """
    winner = None
    
    #checks if there is winner in row
    for row in board:
        if len(set(row)) == 1:
            if row[0] == 'X':
                winner = X
                break
            elif row[0] == 'O':
                winner = O
                break
            
    #check for win in columns
    if winner != X and winner != O: #no winner found in rows
        tempBoard =  [[board[0][0], board[1][0], board[2][0]],
                      [board[0][1], board[1][1], board[2][1]],
                      [board[0][2], board[1][2], board[2][2]],]
        for row in tempBoard:
            if len(set(row)) == 1:
                if row[0] == 'X':
                    winner = X
                    break
                elif row[0] == 'O':
                    winner = O
                    break
                
    #check for win in diagonals
    if winner != X and winner != O: #no winner found in rows or columns
        #left to right diagonal win
        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == 'X':
                winner = X
            elif board[0][0] == 'O':
                winner = O
        #right to left diagonal win
        if board[0][2] == board[1][1] == board[2][0]:
            if board[0][2] == 'X':
                winner = X
            elif board[0][2] == 'O':
                winner = O
    
    print("Current Winner:", winner, '\n')
    return winner
    
    raise NotImplementedError

"""TESTING THINGS FOR OURSELVES!"""
board = initial_state()
#x moves 1
player(board)
actions(board)
xmove1 = result(board, (2, 0))
winner(xmove1)
#o moves 1
player(xmove1)
actions(xmove1)
omove1 = result(xmove1, (0, 0))
winner(omove1)
#x moves 2
player(omove1)
actions(omove1)
xmove2 = result(omove1, (1, 1))
winner(xmove2)
#o moves 2
player(xmove2)
actions(xmove2)
omove2 = result(xmove2, (1, 0))
winner(omove2)
#x moves 3 and wins
player(omove2)
actions(omove2)
xmove3 = result(omove2, (0, 2))
winner(xmove3)
'''
#o moves 3 and wins
player(xmove3)
actions(xmove3)
omove3 = result(xmove3, (2, 2))
winner(omove3)
'''

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    
    The terminal function should accept a board as input and return a boolean value indicating
    whether the game is over.
    o If the game is over, either because someone has won the game or because all cells have
    been filled without anyone winning, the function should return True.
    o Otherwise, the function should return False if the game is still in progress
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    
    The utility function should accept a terminal board as input and output the utility of the board.
    o If X has won the game, the utility is 1. If O has won the game, the utility is -1. If the game
    has ended in a tie, the utility is 0.
    o You may assume utility will only be called on a board if terminal(board) is True.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    
    The minimax function should take a board as input and return the optimal move for the player
    to move on that board.
    o The move returned should be the optimal action (i, j) that is one of the allowable actions
    on the board. If multiple moves are equally optimal, any of those moves is acceptable.
    o If the board is a terminal board, the minimax function should return None.

    """
    raise NotImplementedError