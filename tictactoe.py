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
    """
    #Counts number of x's and o's on board.
    tempX = 0
    tempO = 0
    currPlayer = X
    for row in board:
        for col in row:
            if(col == 'X'):
                tempX += 1
            elif(col == 'O'):
                tempO += 1
    
    #Determines current player based on x's and o's on board.
    if(board == initial_state()): #X plays first.
        currPlayer = X
    elif(tempX < tempO): #There are less x's than o's on the board.
        currPlayer = X
    elif(tempX > tempO): #There are more x's than o's on the board.
        currPlayer = O
    
    return currPlayer
    
    raise NotImplementedError

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #Iterates through board and appends tuple of empty spot to a list.
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
    """
    #Makes a deep copy of input board.
    newBoard = copy.deepcopy(board)
    
    #Changes board based on user input.
    row, col = action
    if(newBoard[row][col] == EMPTY): #Spot user selects is empty, places either X or O
        newBoard[row][col] = player(newBoard)
    elif(newBoard[row][col] != EMPTY): #Spot user selects is not empty, returns an error
        raise ValueError
    
    #FOR TESTING PURPOSES, DELETE IN FINAL
    for row in newBoard:
        print(row)
    
    return newBoard

    raise NotImplementedError

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = None
    
    #Check for a win in a row.
    for row in board:
        if len(set(row)) == 1:
            if row[0] == 'X':
                winner = X
                break
            elif row[0] == 'O':
                winner = O
                break
            
    #Check for a win in a column.
    if winner != X and winner != O: #no winner found in rows
        #Transposes board horizontally in order to use row checking logic.
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
                
    #Check for a win in a diagonal.
    if winner != X and winner != O: #No winner is found in rows or columns.
        #Left to right diagonal win
        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == 'X':
                winner = X
            elif board[0][0] == 'O':
                winner = O
        #Right to left diagonal win
        if board[0][2] == board[1][1] == board[2][0]:
            if board[0][2] == 'X':
                winner = X
            elif board[0][2] == 'O':
                winner = O
    
    #FOR TESTING PURPOSES, DELETE IN FINAL
    print("Current Winner:", winner, '\n')
    return winner
    
    raise NotImplementedError

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #If there is no winner found in the winner function, return false.
    if (winner(board) != None):
        return False
    
    #Check for the number of open spots on board.
    open_spots = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                open_spots += 1
    if (open_spots == 0): #There are no open spots, and the game ends in a tie.
        return True
    else:
        return False
    
    raise NotImplementedError

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #Set utility function based on the winner that the winner function returns.
    utility = 0
    if (winner(board) == X):
        utility = 1
    elif (winner(board) == O):
        utility = -1
    elif (winner(board) == None):
        utility = 0
        
    return utility
    
    raise NotImplementedError

"""TESTING THINGS FOR OURSELVES, DELETE FOR FINAL!"""
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
utility(omove2)
#x moves 3 and wins
player(omove2)
actions(omove2)
xmove3 = result(omove2, (0, 2))
winner(xmove3)
utility(xmove3)
'''
#o moves 3 and wins
player(xmove3)
actions(xmove3)
omove3 = result(xmove3, (2, 2))
winner(omove3)
'''

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