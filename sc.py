"""
Let's play Tic-Tac-Toe!

Instructions:
1. Design/Spec It Out Together
2. Get to writing the code


Specifications: 
 - Create a NxN board>
 - The user determines the size of the board>
 - The User always goes first and is always 'X'>
 - Take input from the user to place 'X' on the board. No data validation needed on the user input. Assume they enter correctly eg: 1,1; 2,2;
 - Choice of the computer is completely random but it can't place over an existing 'X' or 'O'
 - Display the state of the board after each turn.
 - The game is won if either User or Computer has a complete row, column or diagonals. Display appropriate message and end the game. 
 - If no one wins, the game is said to be a draw. 

 Note:
 - You are encouraged to use documentation and stack overflow to help you with the syntax/issues you run into while trying to create the game. However, you are not allowed to look up the solution to the question directly. 
"""

"""
Design-
 - Revisit each specification
 - Create global variables that will be used thru entire programm
 - Creating a run / play function that runs. In this case: __main__
 - Creating a function per specification where appropriate:
  * function `user_input` which starts game, obtains board size, and it's also going to create board (probably as a while loop)
  * function `display_board` which actually prints the board: with empty values of '-' || 
  * check for winner function (or draw)
  
  print("\n")
  print(['-', '-', '-'])
  print(['-', '-', '-'])
  print(['-', '-', '-'])
  print("\n")
  - 'human' = 'X' || place inside functions as 'global human'
  - 

Flow-

 - Get the board size - 3
 - Initialize an empty board
 - Print board

 ----
 - Ask for the users move - 1,1 0,0, 2,1
 - Display board
 - Check for winner
 - Computer move
 - Display board
 - Check for winner
 - Repeat
 ----

"""
import random

def __main__():
    board = []
    human = "X"
    pc = "O"
    game_still_going = True
    user_input = 0

    def get_user_input():
        global user_input
        user_input = int(input("Choose a number from 1 to 3: "))
        for i in range(user_input):
            board.append([])
            for j in range(user_input):
                board[i].append('-')

    def print_board():
        for row in board:
            print(row)

    def user_move():
        move = input("Choose your coordinates/move: ")
        clean_move = move.split(",")
        row = int(clean_move[0])
        column = int(clean_move[1])
        board[row][column] = "X"

    def computer_move():
        while True:
            row = random.randint(0, len(board) - 1)
            column = random.randint(0, len(board) - 1)
            if board[row][column] == "-":
                board[row][column] = "O"
                print(f"the genius pc did this: {row},{column}")
                return

    def check_for_winner(player):
        row_win()
        # column_win()

    def row_win():
        for row in board:
            count = row.count(player)
            print(count, user_input)
            if count == user_input:
                winner = player
                game_still_going = False

    # def column_win():
    #     for column in board:
    #         count = column.count(player)
    #         print(count)
    #         if count == user_input:
    #             winner = player
    #             game_still_going = False

        # asc_diagonal_win
        # desc_diagonal_win

        row_win()
        # column_win()


    get_user_input()

    while game_still_going:
        print_board()
        user_move()
        print_board()
        check_for_winner('X')
        computer_move()
        check_for_winner('O')


__main__()