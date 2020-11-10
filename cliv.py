### Requirenments
"""
* Create a board:
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
#---------GLOBAL VARIABLES------------
# Game board
board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

# Who won?
winner = None

# Keep playing by default
game_still_going = True

# Turn
current_player = "X"

#----------FUNCTIONS-----------------

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def handle_turn(player):
    print(player + "'s turn.")
    user_input = input("Choose a position from 1 to 9: ")

    try:
        position = int(user_input)
        position = int(user_input) - 1
        if position not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            print("Sorry not an option, please try with position form 1 to 9")
        else:
            board[position] = player
            display_board()
    except:
        print("Sorry, I can only handle numbers from 1 to 9")


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    colum_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    # get winner
    if row_winner:
        winner = row_winner
    elif colum_winner:
        winner = colum_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
    global game_still_going

    row_1 = board[0] == board[1] == board[2]
    row_2 = board[3] == board[4] == board[5]
    row_3 = board[6] == board[7] == board[8]
    # if any rows win, stop the game
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None
    

def check_columns():
    global game_still_going

    column_1 = board[0] == board[3] == board[6]
    column_2 = board[1] == board[4] == board[7]
    column_3 = board[2] == board[5] == board[8]
    # if any columns win, stop the game
    if column_1 or column_2 or column_3:
        game_still_going = False
    # return winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None


def check_diagonals():
    global game_still_going

    diagonal_1 = board[0] == board[4] == board[8]
    diagonal_2 = board[6] == board[4] == board[2]
    # if any diagonals win, stop the game
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # return winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    else:
        return None

def check_if_tie():
    pass


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    pass


def play_game():
    # calls prev functions to display board
    display_board()

    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    # the game has ended
    if winner == "X" or winner == "O":
        print(winner + " won!")
    elif winner == None:
        print("Tie.")

play_game()