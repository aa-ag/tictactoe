import pygame, sys
import numpy as np

pygame.init()

# Constants
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
X_WIDTH = 25
BACKGROUND = (28, 170, 156)
LINES = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
X_COLOR = (66, 66, 66)
SPACE = 55

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BACKGROUND)

# Board
board = np.zeros((BOARD_ROWS, BOARD_COLS))
# print(board)

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
    return 0 in board

player = 1

# TESTING
# square_move(0, 0, 1)
# square_move(0, 1, 1)
# square_move(0, 2, 1)
# square_move(1, 0, 1)
# square_move(1, 1, 1)
# square_move(1, 2, 1)
# square_move(2, 0, 1)
# square_move(2, 1, 1)
# square_move(2, 2, 1)
# print(board)
# print(square_available(0,0))
# square_move(0,0,1)
# print(square_available(0,0))
# print(full_board())

draw_lines()

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_y = event.pos[1]
            mouse_x = event.pos[0]
            
            clicked_row = int(mouse_y // 200)
            clicked_col = int(mouse_x // 200)
            
            if square_available(clicked_row, clicked_col):
                if player == 1:
                    square_move(clicked_row, clicked_col, 1)
                    player = 2
                elif player == 2:
                    square_move(clicked_row, clicked_col, 2)
                    player = 1
                draw_figures()

    pygame.display.update()

# TO DO: playing chips, playing functions || conda env: ttt