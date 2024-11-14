import pygame, sys
from numpy.random import randint

from constants import *
import random

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Whack a Mole')


def draw_grid():
    # Draw horizontal lines
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * SQUARE_SIZE),
            (SCREEN_WIDTH, i * SQUARE_SIZE),
            LINE_WIDTH
        )
    # Draw vertical lines
    for i in range(1, BOARD_COLS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * SQUARE_SIZE, 0),
            (i * SQUARE_SIZE, SCREEN_HEIGHT),
            LINE_WIDTH
        )


# Load and scale the mole image
mole_image = pygame.image.load('mole-image.png')
scaled_mole_image = pygame.transform.scale(mole_image, (32, 32))

# Fill background and draw grid
screen.fill(BG_COLOR)
draw_grid()

# Set the initial mole position
mole_rect = scaled_mole_image.get_rect(topleft=(0, 0))
screen.blit(scaled_mole_image, mole_rect)
pygame.display.update()

while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mole_rect.collidepoint(mouse_pos):
                # Move mole to a random position on the grid
                new_x = randint(0, SCREEN_WIDTH // 32)
                new_y = randint(0, SCREEN_HEIGHT // 32)
                mole_rect = scaled_mole_image.get_rect(topleft=(new_x * 32, new_y * 32))

                # Print mouse position for debugging
                print(mouse_pos)

        # Redraw background, grid, and mole in the new position
        screen.fill(BG_COLOR)
        draw_grid()
        screen.blit(scaled_mole_image, mole_rect)
        pygame.display.update()
