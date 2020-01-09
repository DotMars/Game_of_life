# Conway's game of life

import pygame
from pygame import *
import numpy as np

WIN_WIDTH = 221
WIN_HEIGHT = 221

GRID_W = int((WIN_WIDTH - 1 - WIN_WIDTH/10)/10)
GRID_H = 20


grid = (np.arange(0, GRID_W), np.arange(0, GRID_W))
grid = [0 for i in range(GRID_W) for j in range(GRID_H)]
grid = np.array([np.arange(GRID_W), np.arange(GRID_H)])


BLOCK_SIZE = (10, 10)

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0


BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)


def draw_block(screen, grid_w = 0, grid_h = 0):
    # block_pos_x = int(pygame.mouse.get_pos()[0]/BLOCK_SIZE[0])*BLOCK_SIZE[0]
    # block_pos_y = int(pygame.mouse.get_pos()[1]/BLOCK_SIZE[1])*BLOCK_SIZE[1]
    block_pos_x = grid_w[int(pygame.mouse.get_pos()[0]/BLOCK_SIZE[0])]
    block_pos_y = grid_h[int(pygame.mouse.get_pos()[1]/BLOCK_SIZE[1])]

    pygame.draw.rect(screen, RED, (block_pos_x, block_pos_y, BLOCK_SIZE[0], BLOCK_SIZE[1]))
    print(int(pygame.mouse.get_pos()[0]/BLOCK_SIZE[0]))
    print(int(pygame.mouse.get_pos()[1]/BLOCK_SIZE[1]))

def check_neighborhood(pos):
    pass


def generate_grid_points(block_Size, max_position):
    return np.arange(0, max_position, block_Size)


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
    GRID_H = generate_grid_points(BLOCK_SIZE[1], WIN_HEIGHT)
    print(GRID_W)
    for w in GRID_W:
        pygame.draw.line(line, BLACK, (0, w), (w, WIN_HEIGHT))
        screen.blit(line, (w, 0))

    size = (WIN_WIDTH, 1)
    line = pygame.Surface(size)

    for h in GRID_H:
        pygame.draw.line(line, BLACK, (0, h), (WIN_WIDTH, h))
        screen.blit(line, (0, h))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit("QUIT")
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                raise SystemExit("ESCAPE")
            if event.type == KEYDOWN and event.key == K_KP_ENTER:
                print("Game of life starting")
            if event.type == MOUSEBUTTONUP:
                draw_block(screen, GRID_W, GRID_H)
                
                
        pygame.display.update()

main()