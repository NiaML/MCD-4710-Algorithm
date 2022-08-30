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
    new_board = []
    row_size = 3
    col_size = 3
    for row in range(row_size):
        new_board.append([])
        for col in range(col_size):
            new_board[row].append('-')
    return new_board
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

    # return the visual board
    print(  f"-------------\n" +\
            f"| {board[0][0]} | {board[0][1]} | {board[0][2]} |\n"+\
            f"-------------\n"+\
            f"| {board[1][0]} | {board[1][1]} | {board[1][2]} |\n"+\
            f"-------------\n"+\
            f"| {board[2][0]} | {board[2][1]} | {board[2][2]} |\n"+\
            f"-------------")
    


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
    player_win = False
    computer_win = False
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] == player:
            player_win    = True
            break
        elif row[0] == row[1] == row[2] == computer:
            computer_win  = True
            break

    # check columns
    if not player_win and not computer_win:
        for col in range(len(board)):
            if board[0][col] == board[1][col] == board[2][col] == player:
                player_win    = True
                break
            elif board[0][col] == board[1][col] == board[2][col] == computer:
                computer_win  = True
                break

    # check diagonals
    if not player_win and not computer_win and not board[1][1] == '-':
        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == player:
                player_win    = True
            elif board[0][0] == computer:
                computer_win  = True
        elif board[0][2] == board[1][1] == board[2][0]:
            if board[0][2] == player:
                player_win    = True
            elif board[0][2] == computer:
                computer_win  = True
        

    # print statment and return value
    if player_win:
        print('Congrats!! You win!')
        return True
    elif computer_win:
        print('I win! Nice try!')
        return True
    return False



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
    # check if cell is empty then update, else return False
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False
    
    if board[row][col] == player or board[row][col] == computer:
        return False
    board[row][col] = player
    return True

    

# Task 6
# Add additional functions as required
def check_box(board, row, col):
    return board[row][col]

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
        while not update_board(board,row,col,computer):
            row = random.randint(0,2)
            col = random.randint(0,2)
        return (row,col)

    # hard level
    elif level == 'hard':
        row = 0
        col = 0
        # two in a row
        if board[1][1] == board[0][0] and check_box(board,2,2) == '-':
            row = 2
            col = 2

            
        update_board(board,row,col,computer)
        return (row,col)


    

        
# Task 7
from time import sleep
def play():
    """
    Test this function interactively by running - ie. by playing the game
    """
    clear()
    # Add your code here
    # init game settings
    board = init_board()
    level = input('Enter level (easy/hard): ')

    # game loop
    while not is_filled(board):
        clear()
        print_board(board)

        # player's turn
        print('Your turn (input 1 ~ 3)')
        row = int(input('Enter row: '))
        col = int(input('Enter column: '))
        while not update_board(board,row,col,player):
            clear()
            print_board(board)
            print('Invalid move! Try again using 1 ~ 3')
            row = int(input('Enter row: '))
            col = int(input('Enter column: '))
        clear()
        print_board(board)

        # check game condition
        if player_won(board):
            break
        elif is_filled(board):
            print("It's a tie")
            break
        sleep(1)

        # computer's turn
        next_move(board,level)
        clear()
        print_board(board)
        
        # check game condition
        if player_won(board):
            break
        elif is_filled(board):
            print("It's a tie")
            break
        sleep(1)
        



# extra function for clear screen
import os
def clear():
    # for windows
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    
                 
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    play()

