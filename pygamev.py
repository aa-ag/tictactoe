import pygame, sys
import numpy as np

pygame.init()

# Constants
## measures
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
X_WIDTH = 25
## colors
BACKGROUND = (255, 255, 255)
LINES = (0, 0, 0)
CIRCLE_COLOR = (100, 100, 100)
X_COLOR = (50, 50, 50)
SPACE = 55

# Screen

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe -- press "r" to restart')
screen.fill(BACKGROUND)

# Board
board = np.zeros((BOARD_ROWS, BOARD_COLS))

# Functions
def draw_lines():
    '''
    Draws lines in pygame screen
    '''
    # 1st horizontal line
    pygame.draw.line(screen, LINES, (0, 200), (600, 200), LINE_WIDTH)
    # 2nd horizontal line
    pygame.draw.line(screen, LINES, (0, 400), (600, 400), LINE_WIDTH)
    
    # 1st vertical line
    pygame.draw.line(screen, LINES, (200, 0), (200, 600), LINE_WIDTH)
    # 2nd vertical line
    pygame.draw.line(screen, LINES, (400, 0), (400, 600), LINE_WIDTH)


def draw_figures():
    '''
    '''
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * 200 + 200 / 2), int(row * 200 + 200 / 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, X_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), X_WIDTH)
                pygame.draw.line(screen, X_COLOR, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), X_WIDTH)


def square_move(row, col, player):
    '''
    Assigns position to player "move"
    '''
    board[row][col] = player


def square_available(row, col):
    '''
    Checks if board is full
    '''
    return board[row][col] == 0


def full_board():
    '''
    Checks if game is over: no empty spaces left
    '''
    return 0 in board


def check_win(player):
    '''
    Checks if either player has won, either by
    drawing a vertical line, a horizonal line or 
    a diagonal line, asc or descending
    '''
    # checks for vertical "col" wins
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_win(col, player)
            return True

    # checks for horizontal "row" wins
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player  and board[row][2] == player:
            draw_horizontal_win(row, player)
            return True

    # checks for diagonal "ascending" wins
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal_win(player)
        return True

    # checks for diagonal "descending" wins
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal_win(player)
        return True 

    return False


def draw_vertical_win(col, player):
    '''
    Draws vertical line to show vertical win
    '''
    pos_x = col * 200 + 100

    if player == 1:
        color = CIRCLE_COLOR
    else:
        color = X_COLOR

    pygame.draw.line(screen, color, (pos_x, 15), (pos_x, HEIGHT - 15), 15)


def draw_horizontal_win(row, player):
    '''
    Draws horizonal line to show horizontal win
    '''
    pos_y = row * 200 + 100

    if player == 1:
        color = CIRCLE_COLOR
    else:
        color = X_COLOR

    pygame.draw.line(screen, color, (15, pos_y), (WIDTH - 15, pos_y), 15)


def draw_asc_diagonal_win(player):
    '''
    Draws diagonal ascending, left-to-tight line to show win
    '''
    if player == 1:
        color = CIRCLE_COLOR
    else:
        color = X_COLOR

    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)


def draw_desc_diagonal_win(player):
    '''
    Draws diagonal descending, right-to-left line to show win
    '''
    if player == 1:
        color = CIRCLE_COLOR
    else:
        color = X_COLOR
    
    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)


def restart():
    '''
    Allows users to restart after one player has won, or they reached "game over" by
    redrawing the board, its lines, resetting player to "1" and all values in board to zero
    '''
    screen.fill(BACKGROUND)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0
    

draw_lines()

# Variables
player = 1
game_over = False

# main loop
while True:
    '''
    Runs program (game) until players quit, or there are no more moves left, or one player wins
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_y = event.pos[1]
            mouse_x = event.pos[0]
            
            clicked_row = int(mouse_y // 200)
            clicked_col = int(mouse_x // 200)
            
            if square_available(clicked_row, clicked_col):
                if player == 1:
                    square_move(clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over = True
                    player = 2
                    
                elif player == 2:
                    square_move(clicked_row, clicked_col, 2)
                    if check_win(player):
                        game_over = True
                    player = 1
                
            draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                game_over = False

    pygame.display.update()

# TESTING
# print(board) # empty board
# square_move(0, 0, 1)
# square_move(0, 1, 1)
# square_move(0, 2, 1)
# square_move(1, 0, 1)
# square_move(1, 1, 1)
# square_move(1, 2, 1)
# square_move(2, 0, 1)
# square_move(2, 1, 1)
# square_move(2, 2, 1)
# print(board) # completely full
# print(square_available(0,0))
# square_move(0,0,1)
# print(square_available(0,0))
# print(full_board())
# NOTES: conda env: ttt