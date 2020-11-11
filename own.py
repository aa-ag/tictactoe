#--------REQUIREMENTS----------

'''
* Create global variables:
    - board
    - game_is_on
    - winner
    - current_player
* Create board
* Check if board is full
* Check for a win: 
    - vertical win
    - horizontal win
    - diagonal win
* Flip turns
* Quit game
* Run program
'''

#------VARIABLES--------------

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_is_on = True

winner = None

current_player = "X"

#------FUNCTIONS--------------

def display_formatted_board():
    '''
    Formats and displays global variable board
    '''
    print('\n')
    print(board[0] + ' | ' + board[1] + ' | ' + board[2] + '     1 | 2 | 3')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5] + '     4 | 5 | 6')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8] + '     7 | 8 | 9')
    print('\n')


def play_game():
    '''
    Executes all other functions until there's a winner or the game ends
    '''
    global game_is_on

    display_formatted_board()

    while game_is_on:
        handle_turn(current_player)
        flip_player()
        check_gameover()
        if winner == "X" or winner == "O":
            print(f"{winner} won!")
            game_is_on = False
        elif "-" not in board and winner == None:
            print("No winner today, try again!")
            game_is_on = False

def check_gameover():
    check_for_win()


def handle_turn(current_player):
    print(f"It's {current_player}'s turn. ")
    position = input("Choose a number from 1 to 9: ")

    index_in_board = int(position) - 1

    if board[index_in_board] == "-":
        board[index_in_board] = current_player
    else:
        print("Someone else already played that box, try again!")
        handle_turn(current_player)

    display_formatted_board()


def flip_player():
    '''
    Flips player from "X" to "O" and vice versa
    '''
    global current_player
    
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


def check_for_win():
    global winner

    # check if there's a winner in rows
    row_winner = row_win()
    # check if there's a winner in columns
    column_winner = column_win()
    # check if there's a winner in diagonals
    diagonal_winner = diagnonal_win()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner


def row_win():
    global game_is_on

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None


def column_win():
    global game_is_on

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None

def diagnonal_win():

    global game_is_on

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    else:
        return None
    pass

#------EXECUTE PROGRAM--------------

play_game()