# Conway's game of life


################# Rules ########################################################################################
def underpopulation(x): #Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    if x < 2: 
        return 1
    else: 
        return 0
def next_generation(x): #Any live cell with two or three live neighbours lives on to the next generation.
    if x == 2 or x == 3:
        return 1
    else:
        return 0
def overpopulation(x): #Any live cell with more than three live neighbours dies, as if by overpopulation.
    if x > 3:
        return 1
    else: 
        return 0
def reproduction(x): #Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    if x == 3:
        return 1
    else: 
        return 0


import pygame
from pygame import *
import numpy as np
import time

WIN_WIDTH = 500
WIN_HEIGHT = 500

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

def draw_block():
    i = int(pygame.mouse.get_pos()[0]/BLOCK_SIZE[0])
    j = int(pygame.mouse.get_pos()[1]/BLOCK_SIZE[1])

    global grid
    if grid[i][j] == False :
        grid[i][j] = True
    elif grid[i][j] == True:
        grid[i][j] = False

def draw_grid(screen, x_coordinates, y_coordinates, grid):
    screen.fill((255, 255, 255))
    
    for i in range(len(grid)):

        for j in range(len(grid[i])):
            if grid[i][j] == True:
                block_pos_x = x_coordinates[i]
                block_pos_y = y_coordinates[j]

                pygame.draw.rect(screen, BLUE, (block_pos_x, block_pos_y, BLOCK_SIZE[0], BLOCK_SIZE[1]))
               # print("Active life @ X: ", block_pos_x, ", Y: ", block_pos_y)

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

def update_grid(screen, gride):
    global grid
    new_grid = np.copy(grid)
    for i in range(len(grid)):
        iplusone = i + 1
        if iplusone > len(grid)-1 : iplusone = len(grid)-1
        for j in range(len(grid[i])):
            cell = grid[i][j]
            jplusone = j + 1
            if jplusone > len(grid[i])-1: jplusone = len(grid[i])-1

            cell_population = grid[i-1][j-1] + grid[i][j-1] + grid[iplusone][j-1] + grid[i-1][j] + grid[i][j] + grid[iplusone][j] + grid[i-1][jplusone] + grid[i][jplusone] + grid[iplusone][jplusone]

            overpop = 0
            if cell == 1:
                cell_population -= 1
                if underpopulation(cell_population):
                    lonely = (i, j)
                    print("Cell ", lonely, " died of loneliness")
                    new_grid[i][j] = 0

                if overpopulation(cell_population):
                    overpopulated = (i, j)
                    print("Overpopulation at ", overpopulated)
                    new_grid[i][j] = 0
                    overpop = 1

                if next_generation(cell_population) and overpop == 0:
                    new_grid[i][j] = 1
                    newborn = (i, j)
                    print("New born at ", newborn, overpop)
                

            if reproduction(cell_population) and overpop == 0:
                    reproduced = (i, j)
                    print("Reproduced at", reproduced, grid[i][j])

                    new_grid[i][j] = 1
    grid = np.copy(new_grid)
                    
                    

def generate_grid_points(block_Size, max_position):
    return np.arange(0, max_position, block_Size)


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Conway's game of life")
    timer = pygame.time.Clock()

    running = False

    GRID_W = generate_grid_points(BLOCK_SIZE[0], WIN_WIDTH)
    GRID_H = generate_grid_points(BLOCK_SIZE[1], WIN_HEIGHT)   

    
    draw_grid(screen, GRID_W, GRID_H, grid)

    while 1:
        time.sleep(1/24) #24 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit("QUIT")
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                raise SystemExit("ESCAPE")
            if event.type == KEYDOWN and event.key == K_RETURN:
                running = True
                print("Game of life starting")
            if event.type == MOUSEBUTTONDOWN and running == False:
                draw_block()
                draw_grid(screen, GRID_W, GRID_H, grid)

                # i = int(pygame.mouse.get_pos()[0]/BLOCK_SIZE[0])
                # j = int(pygame.mouse.get_pos()[1]/BLOCK_SIZE[1])

        if running:
            # time.sleep()
            update_grid(screen, grid)
            draw_grid(screen, GRID_W, GRID_H, grid)
            

        pygame.display.update()

main()