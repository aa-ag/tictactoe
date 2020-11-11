### Requirenments
"""
* Create a board and other global variables: 
    - board
    - game_still_going
    - winner
    - current_player
* Display the board
* Full board: gameover
* Check for a win:
    - Vertical win
    - Horizontal win
    - Diagonal win ascending
    - Diagonal win descending
* Play game:
    - Start
    - Turns
    - Quit
    - ReStart
"""

# --------- GLOBAL VARIABLES -----------

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_going = True

winner = None

current_player = "X"

# ------------- FUNCTIONS ---------------

def play_game():
    display_board()

    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

        if winner == "X" or winner == "O":
            print(winner + " won.")


def display_board():
    '''
    Displays board and instruction guide
    '''
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")


def handle_turn(player):
    '''
    Switches turns between players
    '''
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

            position = int(position) - 1

            if board[position] == "-":
                valid = True
            else:
                print("Someone is already there! Try again :)")

    board[position] = player

    display_board()



def check_if_game_over():
    '''
    Checks if game is over
    '''
    check_for_winner()
    check_for_tie()


def check_for_winner():
    '''
    Check to see if somebody has won
    '''
    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None



def check_rows():
    '''
    Check the rows for a win
    '''
    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
        return board[0] 
    elif row_2:
        return board[3] 
    elif row_3:
        return board[6] 
    else:
        return None


def check_columns():
    '''
    Check the columns for a win
    '''
    global game_still_going

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False

    if column_1:
        return board[0] 
    elif column_2:
        return board[1] 
    elif column_3:
        return board[2] 
    else:
        return None



def check_diagonals():
    '''
    Check the diagonals for a win
    '''
    global game_still_going

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0] 
    elif diagonal_2:
        return board[2]
    else:
        return None



def check_for_tie():
    '''
    Check if there is a tie
    '''
    global game_still_going

    if "-" not in board:
        game_still_going = False
        return True
    else:
        return False


def flip_player():
    '''
    Flip the current player from X to O, or O to X
    '''
    global current_player

    if current_player == "X":
        current_player = "O"

    elif current_player == "O":
        current_player = "X"


# ------------ EXECUTE CODE -------------
play_game()