# Conway's game of life

import pygame
from pygame import *
import numpy as np

WIN_WIDTH = 221
WIN_HEIGHT = 221

GRID_W = (WIN_WIDTH - 1 - WIN_WIDTH/10)/10
GRID_H = 20


def get_block_size_From_win_dims(x, y):
    block_x = 10
    block_y = 10
    return (block_x, block_y)


BLOCK_SIZE = get_block_size_From_win_dims(WIN_WIDTH, WIN_HEIGHT)

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0

DEBUG = 0

BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)


def draw_grid(dims=(WIN_WIDTH/10, WIN_HEIGHT/10), block_size=BLOCK_SIZE):
    print(dims)


def check_neighborhood(pos):
    pass


def generate_grid_points(block_Size, max_position):
    return np.arange(0, max_position, block_Size+1)


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Conway's game of life")
    timer = pygame.time.Clock()

    running = True

    screen.fill((255, 255, 255))

    size = (1, WIN_HEIGHT)
    line = pygame.Surface(size)

    GRID_W = generate_grid_points(BLOCK_SIZE[0], WIN_WIDTH)

    for w in GRID_W:
        pygame.draw.line(line, BLACK, (0, w), (w, WIN_HEIGHT))
        screen.blit(line, (w, 0))

    # size = (WIN_WIDTH, 1)
    # line = pygame.Surface(size)
    # for w in range(0, int(GRID_H)):
    #     pygame.draw.line(line, pygame.Color(
    #         0, 0, 0), (0, BLOCK_SIZE[0] * w), (WIN_WIDTH, BLOCK_SIZE[0] * w))
    #     screen.blit(line, (0, BLOCK_SIZE[0]*w))

    pygame.draw.line(line, RED, (0, 0), (0, WIN_HEIGHT))
    screen.blit(line, (0, 0))

    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


main()
