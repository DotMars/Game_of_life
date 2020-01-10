# Conway's game of life

import pygame
from pygame import *
import numpy as np

WIN_WIDTH = 500
WIN_HEIGHT = 500

GRID_W = []
GRID_H = []

BLOCK_SIZE = (10, 10)

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0

# grid = [[False]*int(WIN_WIDTH/BLOCK_SIZE[0])]*int(WIN_HEIGHT/BLOCK_SIZE[1]) ### THIS DOESN'T WORK ###
grid = np.array([[0]*int(WIN_WIDTH/BLOCK_SIZE[0])]*int(WIN_HEIGHT/BLOCK_SIZE[1]), np.int32)

BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)
WHITE = pygame.Color(255,255,255)


def draw_block(screen, grid_w = 0, grid_h = 0):
    i = int(pygame.mouse.get_pos()[0]/BLOCK_SIZE[0])
    j = int(pygame.mouse.get_pos()[1]/BLOCK_SIZE[1])

    block_pos_x = grid_w[i]
    block_pos_y = grid_h[j]
    global grid
    if grid[i][j] == False :
        grid[i][j] = True
        BLOCK_COLOR = BLUE
    else:
        grid[i][j] = False
        BLOCK_COLOR = WHITE

    pygame.draw.rect(screen, BLOCK_COLOR, (block_pos_x, block_pos_y, BLOCK_SIZE[0], BLOCK_SIZE[1]))
    print("Added life at position X: ", i, ", Y: ", j)

def draw_grid(screen, x_coordinates, y_coordinates):
    size = (1, WIN_HEIGHT)
    line = pygame.Surface(size) 
    for w in x_coordinates:
        pygame.draw.line(line, BLACK, (0, w), (w, WIN_HEIGHT))
        screen.blit(line, (w, 0))

    size = (WIN_WIDTH, 1)
    line = pygame.Surface(size)
    for h in y_coordinates:
        pygame.draw.line(line, BLACK, (0, h), (WIN_WIDTH, h))
        screen.blit(line, (0, h))
    



def update_grid():
    pass


def generate_grid_points(block_Size, max_position):
    return np.arange(0, max_position, block_Size)


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Conway's game of life")
    timer = pygame.time.Clock()

    running = False

    screen.fill((255, 255, 255))

    GRID_W = generate_grid_points(BLOCK_SIZE[0], WIN_WIDTH)
    GRID_H = generate_grid_points(BLOCK_SIZE[1], WIN_HEIGHT)   

    while 1:
        draw_grid(screen, GRID_W, GRID_H)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit("QUIT")
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                raise SystemExit("ESCAPE")
            if event.type == KEYDOWN and event.key == K_RETURN:
                running = True
                print("Game of life starting")
            if event.type == MOUSEBUTTONDOWN and running == False:
                draw_block(screen, GRID_W, GRID_H)
                i = int(pygame.mouse.get_pos()[0]/BLOCK_SIZE[0])
                j = int(pygame.mouse.get_pos()[1]/BLOCK_SIZE[1])
                print(grid)

        if running:
            update_grid()

        pygame.display.update()

main()