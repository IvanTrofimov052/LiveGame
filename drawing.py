import pygame
from main import *
# import keyboard
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
all_sprites = pygame.sprite.Group()

sc = pygame.display.set_mode((max_x * 20, max_y * 20 + 50))

class DrawingCell(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((19, 19))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

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
                self.cells[i].append(DrawingCell(i * 20, j * 20))
                all_sprites.add(self.cells[i][j])
    
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

    all_sprites.draw(sc)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            # stop or start game
            if i.key == pygame.K_SPACE:
                stop = not stop
            # make a move when the game a stop
            elif i.key == pygame.K_RIGHT and stop == True:
                a.move()
                pygame.display.update()
            # calculate the previous statu
            elif i.key == pygame.K_DOWN and stop == True:
                a.previous()
                pygame.display.update()

        elif i.type == pygame.MOUSEBUTTONUP and stop == True:
            pos = pygame.mouse.get_pos()
            x = pos[0] // 20
            y = pos[1] // 20

            # try:


            a.field[x][y].alive = not a.field[x][y].alive

            field.move(a)
            # except:
            #     pass
            all_sprites.draw(sc)
            pygame.display.update()
            clock.tick(1)
