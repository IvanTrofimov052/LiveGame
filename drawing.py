import pygame
from main import *
import keyboard
import asyncio
# import keyboard

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)

stop = False

pygame.init()

sc = pygame.display.set_mode((max_x * 20, max_y * 20 + 50))

class DrawingCell():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((19, 19))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()

    def drawing(self, color):
        self.image.fill(color)

class FieldDraw():
    def __init__(self):
        self.cells = []
        for i in range(max_y):
            self.cells.append([])
            for j in range(max_x):
                coords = (i * 20, j * 20, 19, 19)
                # coords = (0,0, 0 + 15, 0 + 15)
                self.cells[i].append(DrawingCell())
                print(coords)
    
    def move(self, calculated_field):
      for i in range(max_y):
        for j in range(max_x):
          coords = (i * 20, j * 20, 19, 19)

          if calculated_field.field[i][j].alive == True:
            self.cells[i][j].drawing(GREEN)
          else:
              self.cells[i][j].drawing(YELLOW)


# making a field
arr = init_field()
a = Field(arr)

# здесь будут рисоваться фигуры

pygame.display.update()

field = FieldDraw()

clock = pygame.time.Clock()

while 1:
    # cheking the stop of game
    if stop == False:
        pygame.display.update()
        clock.tick(1)
        a.move()
    else:
        pass

    field.move(a)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            # stop or start game
            if i.key == pygame.K_SPACE:
                stop = not stop
            # make a move whenthe game a stop
            elif i.key == pygame.K_RIGHT and stop == True:
                a.move()
                pygame.display.update()
