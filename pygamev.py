import pygame, sys
import numpy as np

pygame.init()

# Constants
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
BACKGROUND = (28, 170, 156)
LINES = (23, 145, 135)

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



# TESTING
square_move(0, 0, 1)
square_move(0, 1, 1)
square_move(0, 2, 1)
square_move(1, 0, 1)
square_move(1, 1, 1)
square_move(1, 2, 1)
square_move(2, 0, 1)
square_move(2, 1, 1)
square_move(2, 2, 1)
print(board)
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

            print(clicked_row, clicked_col)
            
    pygame.display.update()

# TO DO: playing chips, playing functions || conda env: ttt