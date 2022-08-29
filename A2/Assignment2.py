# Assignment 2 -    T2 2022
# Name:             Chi Him Lam
# Student ID:       33191654
# Finished on:      
# Last modified on: 


computer = 'O'
player = 'X'
# Template for Assignment 2 - T2 2022
# Add your code below the test cases provided in each function
# Task 1
import random
def init_board():
    """
    Input: No input taken
    Output: A table that represents the 3x3 tic-tac-toe board with all the cells filled with a hyphen

    For example: 
    >>> board = init_board()
    >>> board
    [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    """
    # Add your code here
    output = []
    row_size = 3
    col_size = 3
    for row in range(row_size):
        output.append([])
        for col in range(col_size):
            output[row].append('-')
    return output
    # hard coded version below
    return  [['-', '-', '-'], 
             ['-', '-', '-'], 
             ['-', '-', '-']]



# Task 2
def print_board(board):
    """
    Input: The current status of the board 
    Output: Prints the current board to the screen

    For example: 
    >>> board = init_board()
    >>> print_board(board)
    -------------
    | - | - | - |
    -------------
    | - | - | - |
    -------------
    | - | - | - |
    -------------
    """
    # Add your code here

    # hard coded version below
    return f'-------------' + '\n' + \
           f'| {board[0][0]} | {board[0][1]} | {board[0][2]} |' + '\n' + \
           f'-------------' + '\n' + \
           f'| {board[1][0]} | {board[1][1]} | {board[1][2]} |' + '\n' + \
           f'-------------' + '\n' + \
           f'| {board[2][0]} | {board[2][1]} | {board[2][2]} |' + '\n' + \
           f'-------------'
    


# Task 3
def is_filled(board):
    """
    Input: The current status of the board 
    Output: True if the board is filled, False otherwise

    For example: 
    >>> board = init_board()
    >>> is_filled(board)
    False
    >>> test_board = [['X','O','X'],['O','X','O'],['X','O','X']]
    >>> is_filled(test_board)
    True
    >>> test_board = [['X','O','-'],['O','X','O'],['X','-','X']]
    >>> is_filled(test_board)
    False
    """
    # Add your code here
    # if any cell is '-', then board is not filled
    for row in board:
        for col in row:
            if col == '-':
                return False
    return True

    

# Task 4
# Add additional functions as required
def player_won(board):
    """
    Input: The current status of the board 
    Output: True if the board is filled, False otherwise

    For example: 
    >>> test_board = [['X','O','X'],['O','X','O'],['X','O','X']]
    >>> player_won(test_board)
    Congrats!! You win!
    True
    >>> test_board = [['O','X','O'],['X','O','X'],['O','X','O']]
    >>> player_won(test_board)
    I win! Nice try!
    True
    >>> test_board = [['X','-','O'],['X','-','O'],['X','-','-']]
    >>> player_won(test_board)
    Congrats!! You win!
    True
    >>> test_board = [['O','O','X'],['X','X','O'],['O','X','O']]
    >>> player_won(test_board)
    False
    """
    # Add your code here
    # X is player and O is computer
    player_X = False
    computer_O = False
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] == 'X':
            player_X    = True
        elif row[0] == row[1] == row[2] == 'O':
            computer_O  = True
    # check columns
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] == 'X':
            player_X    = True
        elif board[0][col] == board[1][col] == board[2][col] and board[0][col] == 'O':
            computer_O  = True
    # return value and statement
    if player_X:
        print('Congrats!! You win!')
    elif computer_O:
        print('I win! Nice try!')
    else:
        return False
    return True


# Task 5
def update_board(board,row,col,player):
    """
    Input: The current status of the board, the row, column and the player (‘X’ or ‘O’) for the next move. 
    Output: True if the board is successfully updated, False otherwise.


    For example: 
    >>> test_board = [['X','O','-'],['-','X','-'],['-','O','-']]
    >>> update_board(test_board,1,0,'X')
    True
    >>> test_board = [['X','O','-'],['-','X','-'],['X','O','-']]
    >>> update_board(test_board,2,1,'O')
    False
    """
    # Add your code here
    # check if cell is empty
    if board[row][col] == '-':
        board[row][col] = player
        return True
    return False

    

# Task 6
# Add additional functions as required
                
def next_move(board,level):
    """
    Input: The current status of the board and the difficulty level
    Output: Position of the next move (of the computer), as a tuple (row,column)

    For example: 
    >>> test_board = [['X','-','-'],['X','O','-'],['O','-','-']]
    >>> next_move(test_board,'hard')
    (0, 2)
    >>> test_board = [['-','X','-'],['-','X','O'],['O','-','-']]
    >>> next_move(test_board,'hard')
    (2, 1)

    """
    # Add your code here
    # easy level
    if level == 'easy':
        # get random row and column
        row = random.randint(0,2)
        col = random.randint(0,2)
        while update_board() == False:
            row = random.randint(0,2)
            col = random.randint(0,2)
        return (row,col)
        pass
    elif level == 'hard':
        pass
    return
    

        
# Task 7
def play():
    """
    Test this function interactively by running - ie. by playing the game
    """
    
    # Add your code here
    board = init_board()
    level = input('Enter level (easy/hard): ')
    print_board(board)
    while not is_filled(board) and not player_won(board):
        # player's turn
        row = int(input('Enter row: '))
        col = int(input('Enter column: '))
        if update_board(board,row,col,'X'):
            print_board(board)
        else:
            print('Invalid move!')
        # computer's turn
        if not is_filled(board) and not player_won(board):
            row,col = next_move(board,level)
            update_board(board,row,col,'O')
            print_board(board)


                 
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    play()
