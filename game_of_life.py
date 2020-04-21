###################################
# __name__ = Conway's game of life
# __author__ = "dotMars"
# __license__ = https://www.gnu.org/licenses/gpl-3.0.en.html
###

################# Rules
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

import numpy as np
import time

# Pygame isplay settings
WIN_WIDTH = 500
WIN_HEIGHT = 500

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0

# Grid settings
BLOCK_SIZE = (10, 10)
grid = np.array([[0]*int(WIN_WIDTH/BLOCK_SIZE[0])]*int(WIN_HEIGHT/BLOCK_SIZE[1]), np.int32)

# Pygame colors
BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)
WHITE = pygame.Color(255,255,255)

# Debug
DEBUG = 0

def draw_block():
    """
    A function that draws a block representing a life cell in the grid case where the mouse is currently pointing
    Args : None
    Return : None
    """
    i = int(pygame.mouse.get_pos()[0]/BLOCK_SIZE[0])
    j = int(pygame.mouse.get_pos()[1]/BLOCK_SIZE[1])

    global grid
    if grid[i][j] == False :
        grid[i][j] = True
    elif grid[i][j] == True:
        grid[i][j] = False

def draw_grid(screen, x_coordinates, y_coordinates):
    """
    A function that draws an empty grid on the screen. It's used multiple times to reset the grid.
    Args :  - screen : A pygame surface to draw the grid on
            - x_coordinates : grid lines positions on the x axis
            - y_cooridnates : grid lines positions on the y axis
    """
    global grid
    screen.fill((255, 255, 255))

    for i in range(len(grid)):

        for j in range(len(grid[i])):
            if grid[i][j] == True:
                block_pos_x = x_coordinates[i]
                block_pos_y = y_coordinates[j]

                pygame.draw.rect(screen, BLUE, (block_pos_x, block_pos_y, BLOCK_SIZE[0], BLOCK_SIZE[1]))
                if DEBUG : print("Active life @ X: ", block_pos_x, ", Y: ", block_pos_y)

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

def update_grid(screen):
    """
    A function that translates all the ones in the array grid into active cells on the screen.
    Args : - screen pygame surface to draw the updated grid on
    Return : - None
    """
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

def generate_grid_lines_coordinates(block_size, max_position):
    """
    Returns a range of positions depending on the block size and maximum linear position.
    Args : block_size : size of a single grid block, must be constante for all blocks
    Return : numpy array with grid lines cooridnates
    """
    return np.arange(0, max_position, block_size)


def main():
    """
    Main game function
    """

    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Conway's game of life")

    # A flag for the state of the game of life, becomes True when the player
    # finishes laying out the grid and presses enter
    running = False

    # List of grid lines coordinates on the x axis
    GRID_W = generate_grid_lines_coordinates(BLOCK_SIZE[0], WIN_WIDTH)
    # List of grid lines coordinates on the y axis
    GRID_H = generate_grid_lines_coordinates(BLOCK_SIZE[1], WIN_HEIGHT)

    # Draw the grid on the screen
    draw_grid(screen, GRID_W, GRID_H)

    while 1:
        # Main loop
        time.sleep(1/24) #24 FPS

        # Some event handling
        for event in pygame.event.get():

            # Quit events
            if event.type == pygame.QUIT:
                raise SystemExit("QUIT")
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                raise SystemExit("ESCAPE")

            # Simulation start
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                running = True
                print("Game of life starting")

            # Mouse click
            if event.type == pygame.MOUSEBUTTONDOWN and running == False:
                draw_block()
                draw_grid(screen, GRID_W, GRID_H)

        # If the simulation has started -> update the grid on the screen
        if running:
            update_grid(screen)
            draw_grid(screen, GRID_W, GRID_H)

        # Draw the new frame on the screen
        pygame.display.update()

if __name__ == "__main__":

    main()