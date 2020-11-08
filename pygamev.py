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
print(board)

# Functions
def draw_lines():
    # 1st horizontal line
    pygame.draw.line(screen, LINES, (0, 200), (600, 200), LINE_WIDTH)
    # 2nd horizontal line
    pygame.draw.line(screen, LINES, (0, 400), (600, 400), LINE_WIDTH)
    # 1st vertical line
    pygame.draw.line(screen, LINES, (200, 0), (200, 600), LINE_WIDTH)
    # 2nd vertical line
    pygame.draw.line(screen, LINES, (400, 0), (400, 600), LINE_WIDTH)

draw_lines()

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit

    pygame.display.update()

# TO DO: playing chips, playing functions || conda env: ttt