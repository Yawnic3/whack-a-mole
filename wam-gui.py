import pygame, sys
from constants import *


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Whack a Mole')

def draw_grid():
#draw horizontal lines
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(
        screen,
        LINE_COLOR,
        (0, i * SQUARE_SIZE),
        (SCREEN_WIDTH, i * SQUARE_SIZE),
        LINE_WIDTH
        )
    #draw vertical lines
        for i in range(1, BOARD_COLS):
            pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * SQUARE_SIZE, 0),
            (i * SQUARE_SIZE, SCREEN_HEIGHT),
            LINE_WIDTH
)
screen.fill(BG_COLOR)
draw_grid()
pygame.display.update()  # Initial display update to show grid

while True:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            pygame.display.update()
