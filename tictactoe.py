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



def minimax(board):
    
    '''This function considers each available action from a given board state and runs minimax on each choice.
    The action with the highest minimax value will be returned. The minimax algorithm is defined separately '''

    if terminal(board): # No possible choices if the board is terminal
        return None

    if player(board) == X:
        best_value = -math.inf 
        best_action = None

        #Each possible action in the board needs to be considered
        for action in actions(board):
            
            new_board = result(board, action) #Create a new board to protect the current board from changes
            
            value = minimax_value(new_board, False) #Update the best value and best action
            if value > best_value:
                best_value = value
                best_action = action
        return best_action
    else:
       
        best_value = math.inf    #This code is from the perspective of the minimizing player
        best_action = None
        for action in actions(board):
            
            new_board = result(board, action)
           
            value = minimax_value(new_board, True) #Update the best value, which for the minimizer is the lowest value
            if value < best_value:
                best_value = value
                best_action = action
        return best_action

def minimax_value(board, maximizing_player):
    '''This function is recursive. Each generation of a board state leads to more possible board states to consider
      for the Maximixing/Minimizing player. Once a game has ended, the utility value is returned, and scores
    ripple back up the game tree to return the best choice for the maximixing player'''
    if terminal(board):
        return utility(board)           #When recursion has ended, the end state's value must be returned

    if maximizing_player:
        v = -math.inf
        for action in actions(board): #Consider each action
           
            new_board = result(board, action) #Generate the state that results from that action
            
            v = max(v, minimax_value(new_board, False)) #Recrusively generate more states based on an action for the opponent
        return v
    else:
        v = math.inf
        for action in actions(board):
            
            new_board = result(board, action)
            
            v = min(v, minimax_value(new_board, True))
        return v



    raise NotImplementedError