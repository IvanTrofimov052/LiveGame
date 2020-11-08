#ошибка в том что соседи увеличиваюиться
import random

mode = "normal"

max_x = 40  # this const need to know the max x coordinat
max_y = 40  # this const need to know the max y coordinat


def num_to_binary_system(n):
    b = []

    while n > 0:
        b.append(n % 2)
        n = n // 2

    return b


# this class need to save the position of field
class Field:
    def __init__(self, array):
        self.field = array

    # this function change the field
    def change_field(self, array):
        self.field = array

    # this funcition is returned field as array
    def get_field(self):
        return self.field
    
    # this function is making a move(i + 1) % max_y
    def move(self):
        # there we update live neighbords in all cell
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                self.field[i][j].update_live_neightbord()

        # there we kill or make new cell
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                self.field[i][j].next_die_or_live()


class Cell:
    alive = True
    live_neightbors = 0

    def __init__(self):
        self.neighbors = []

    # this function update live neightbords
    def update_live_neightbord(self):
        self.live_neightbors = 0
        print(len(self.neighbors))
        for j in range(len(self.neighbors)):
            if self.neighbors[j].alive:
                self.live_neightbors += 1

    # this function detect die or live this Cell after the move
    def next_die_or_live(self):
        if mode == "normal":
            # checking die or live cell(it deepens of number of neighborhoods)
            if (self.live_neightbors < 2 or self.live_neightbors > 3) and self.alive == True:
                print(self.live_neightbors, "fck")
                self.alive = False
            elif self.live_neightbors < 2 or self.live_neightbors > 3:
                self.alive = False
            elif self.live_neightbors == 2 and self.alive == False:
                self.alive = False
            else:
                self.alive = True
        else:
            print('fuck')

            if self.live_neightbors >= 2 and self.alive == False:
                self.alive = True

        self.live_neightbors = 0


# this function made the strtest field
def init_field():
    # make a array
    array = []
    # making cell in this array
    for i in range(max_y):
        array.append([])
        for j in range(max_x):
            array[i].append(Cell())
            array[i][j].alive = False
    
    # making link to cell in this array
    for i in range(max_y):
        for j in range(max_x):
            array[i][j].neighbors.append(array[(i - 1) % max_y][j])
            print(len(array[i][j].neighbors), '1')
            array[i][j].neighbors.append(array[(i + 1) % max_y][j])
            array[i][j].neighbors.append(array[i][(j - 1) % max_x])
            array[i][j].neighbors.append(array[i][(j + 1) % max_x])
            array[i][j].neighbors.append(array[(i + 1) % max_y][(j - 1) % max_x])
            array[i][j].neighbors.append(array[(i + 1) % max_y][(j + 1) % max_x])
            array[i][j].neighbors.append(array[(i - 1) % max_y][(j - 1) % max_x])
            array[i][j].neighbors.append(array[(i - 1) % max_y][(j + 1) % max_x])

    print(array[0][0])
    print ( array[0][1] )

    return array


# this function is making a move(i + 1) % max_y
def move(field):
    # there we update live neighbords in all cell
    for i in range(len(field.field)):
        for j in range(len(field.field[i])):
            field.field[i][j].update_live_neightbord()

    # there we kill or make new cell
    for i in range(len(field.field)):
        for j in range(len(field.field[i])):
            field.field[i][j].next_die_or_live()



if __name__ == '__main__':
    # arr = init_field()
    # a = Field(arr)
    # while True:
    #     move(a)
    print(num_to_binary_system(6))