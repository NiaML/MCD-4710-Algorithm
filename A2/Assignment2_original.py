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
    
    if not board[row][col] == '-':
        return False
    board[row][col] = player
    return True

    

# Task 6
# Add additional functions as required
def random_move(board):
    row_index = random.randint(0,2)
    col_index = random.randint(0,2)
    while not update_board(board,row_index,col_index,computer):
        row_index = random.randint(0,2)
        col_index = random.randint(0,2)
    return (row_index,col_index)

# abandoned method as it is too complicated
# # input location to test corresponding location that is available and return a list of the available locations
# def move_available(board,row,col):
#     moves = []
#     # hard coded moves as dynamic detection is too complex for 3x3 board, two holes to ignore for each corner
#     # center
#     # if row == col == 1:
#     #     for i in range(len(board)):
#     #         for j in range(len(board[i])):
#     #             if i == row and j == col:
#     #                 continue
#     #             if not board[i][j] == computer and not board[i][j] == player:
#     #                 moves.append((i,j))
#     # # top left
#     # if row == 0 and col == 0:
#     #     for i in range(len(board)):
#     #         for j in range(len(board[i])):
#     #             if ([i] == 1 and [j] == 2) or ([i] == 2 and [j] == 1):
#     #                 continue
#     #             if not board[i][j] == computer and not board[i][j] == player:
#     #                 moves.append((i,j))
    
    
#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             if i == row and j == col:
#                 continue
#             # top left
#             elif ([i] == 1 and [j] == 2) or ([i] == 2 and [j] == 1) :
#                 continue
#             else: 
#                 if not board[i][j] == computer and not board[i][j] == player:
#                     moves.append((i,j))

#     return moves

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
        return random_move(board)

# next move instructions
# 1. If there are two ‘O’s in a row, column or a diagonal, the next move should fill thecorresponding row, column or diagonal with another ‘O’ so that the computer wins.
# 2. If there are two ‘X’ s in a row, column or a diagonal, the next move should fill the corresponding row, column or diagonal with an ‘O’ so that the computer blocks the user’s next winning move.
# 3. If there is an ‘O’ in a row, column or a diagonal, the next move should place another ‘O’ on the same row, column or diagonal.
# 4. If there are no ‘O’s on the board, place an ‘O’ in any random available position.
    # hard level
    elif level == 'hard':
        row_index = 0
        col_index = 0
        # for computer win condition
        # two in a row
        for row in range(len(board)):
            if board[row][0] == board[row][1] == computer:
                row_index = row
                col_index = 2
                if update_board(board,row_index,col_index,computer):
                    return (row_index,col_index)
            elif board[row][0] == board[row][2] == computer:
                col_index = row
                row_index = 1
                if update_board(board,row_index,col_index,computer):
                    return (row_index,col_index)
            elif board[row][1] == board[row][2] == computer:
                col_index = row
                row_index = 0
                if update_board(board,row_index,col_index,computer):
                    return (row_index,col_index)

        # two in a column
        for col in range(len(board)):
            if board[0][col] == board[1][col] == computer:
                row_index = 2
                col_index = col
                if update_board(board,row_index,col_index,computer):
                    return (row_index,col_index)
            elif board[0][col] == board[2][col] == computer:
                row_index = 1
                col_index = col
                if update_board(board,row_index,col_index,computer):
                    return (row_index,col_index)
            elif board[1][col] == board[2][col] == computer:
                row_index = 0
                col_index = col
                if update_board(board,row_index,col_index,computer):
                    return (row_index,col_index)

        # two in a diagonal
        if board[0][0] == board[1][1] == computer:
            row_index = 2
            col_index = 2
            if update_board(board,row_index,col_index,computer):
                return (row_index,col_index)
        elif board[0][0] == board[2][2] == computer:
            row_index = 1
            col_index = 1
            if update_board(board,row_index,col_index,computer):
                return (row_index,col_index)
        elif board[1][1] == board[2][2] == computer:
            row_index = 0
            col_index = 0
            if update_board(board,row_index,col_index,computer):
                return (row_index,col_index)
        elif board[0][2] == board[1][1] == computer:
            row_index = 2
            col_index = 0
            if update_board(board,row_index,col_index,computer):
                return (row_index,col_index)
        elif board[0][2] == board[2][0] == computer:
            row_index = 1
            col_index = 1
            if update_board(board,row_index,col_index,computer):
                return (row_index,col_index)
        elif board[1][1] == board[2][0] == computer:
            row_index = 0
            col_index = 2
            if update_board(board,row_index,col_index,computer):
                return (row_index,col_index)

        # for blocking user win condition (basically a copy of above, line 237~302)
        # two in a row
        for row in range(len(board)):
            if board[row][0] == board[row][1] == player:
                row_index = row
                col_index = 2
                if update_board(board,row_index,col_index,computer):
                    return (row_index,col_index)
            elif board[row][0] == board[row][2] == player:
                col_index = row
                row_index = 1
                if update_board(board,row_index,col_index,computer):
                    return (row_index,col_index)
            elif board[row][1] == board[row][2] == player:
                col_index = row
                row_index = 0
                if update_board(board,row_index,col_index,computer):
                    return (row_index,col_index)

        # two in a column
        for col in range(len(board)):
            if board[0][col] == board[1][col] == player:
                row_index = 2
                col_index = col
                if update_board(board,row_index,col_index,computer):
                    return (row_index,col_index)
            elif board[0][col] == board[2][col] == player:
                row_index = 1
                col_index = col
                if update_board(board,row_index,col_index,computer):
                    return (row_index,col_index)
            elif board[1][col] == board[2][col] == player:
                row_index = 0
                col_index = col
                if update_board(board,row_index,col_index,computer):
                    return (row_index,col_index)

        # two in a diagonal
        if board[0][0] == board[1][1] == player:
            row_index = 2
            col_index = 2
            if update_board(board,row_index,col_index,computer):
                return (row_index,col_index)
        elif board[0][0] == board[2][2] == player:
            row_index = 1
            col_index = 1
            if update_board(board,row_index,col_index,computer):
                return (row_index,col_index)
        elif board[1][1] == board[2][2] == player:
            row_index = 0
            col_index = 0
            if update_board(board,row_index,col_index,computer):
                return (row_index,col_index)
        elif board[0][2] == board[1][1] == player:
            row_index = 2
            col_index = 0
            if update_board(board,row_index,col_index,computer):
                return (row_index,col_index)
        elif board[0][2] == board[2][0] == player:
            row_index = 1
            col_index = 1
            if update_board(board,row_index,col_index,computer):
                return (row_index,col_index)
        elif board[1][1] == board[2][0] == player:
            row_index = 0
            col_index = 2
            if update_board(board,row_index,col_index,computer):
                return (row_index,col_index)

        # placing the computer's move corresponding to the its existing moves
        
        
        # no computer's move on the board
        computer_move_exists = False
        while not computer_move_exists:
            for row in range(len(board)):
                for col in range(len(board[row])):
                    if board[row][col] == computer:
                        computer_move_exists = True
                        break
        if not computer_move_exists:
            return random_move(board)


    

        
# Task 7
from time import sleep
def play():
    """
    Test this function interactively by running - ie. by playing the game
    """
    # Add your code here
    clear()
    # init game settings
    print("Welcome to PVE Tic-Tac-Toe!")
    board = init_board()
    level = input('Enter level (easy/hard): ')
    while level != 'easy' and level != 'hard':
        print('Invalid input! Please try again.')
        level = input('Enter level (easy/hard): ')

    # game loop
    while not is_filled(board):
        clear()
        print_board(board)

        # player's turn
        print('Your turn (input 0 ~ 2)')
        row = int(input('Enter row: '))
        col = int(input('Enter column: '))
        while not update_board(board,row,col,player):
            clear()
            print_board(board)
            print('Invalid move! Try again using 0 ~ 2')
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

