import pygame
from main import *
# import keyboard

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)

pygame.init()

sc = pygame.display.set_mode((max_x * 200, max_y * 200 + 50))


class FieldDraw():
    def __init__(self):
        cells = []
        for i in range(max_y):
            cells.append([])
            for j in range(max_x):
                coords = (i * 20, j * 20, i * 20 + 15, j * 20 + 15)
                # coords = (0,0, 0 + 15, 0 + 15)
                cells[i].append(pygame.draw.rect(sc, WHITE, coords))
                print(coords)



# здесь будут рисоваться фигуры

pygame.display.update()

field = FieldDraw()

while 1:
    pygame.display.update()
    pygame.time.delay(1000)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()