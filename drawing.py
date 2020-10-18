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

sc = pygame.display.set_mode((max_x * 20, max_y * 20 + 50))


class FieldDraw():
    def __init__(self):
        self.cells = []
        for i in range(max_y):
            self.cells.append([])
            for j in range(max_x):
                coords = (i * 20, j * 20, 19, 19)
                # coords = (0,0, 0 + 15, 0 + 15)
                self.cells[i].append(pygame.draw.rect(sc, WHITE, coords))
                print(coords)
    
    def move(self, calculated_field):
      for i in range(max_y):
        for j in range(max_x):
          coords = (i * 20, j * 20, 19, 19)
          if calculated_field.field[i][j].alive == True:
            self.cells[i][j] = pygame.draw.rect(sc, GREEN, coords)
          else:
            self.cells[i][j] = pygame.draw.rect(sc, YELLOW, coords)


# making a field
arr = init_field()
a = Field(arr)

# здесь будут рисоваться фигуры

pygame.display.update()

field = FieldDraw()

clock = pygame.time.Clock()

while 1:
    pygame.display.update()
    pygame.time.delay(2000)
    a.move()
    field.move(a)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
