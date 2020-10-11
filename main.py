# в ходе должнобыть вычисление соседедей у каждой клетки потом уюийсвто и ли оставление в живых рождение
# сделать ссылки на соседей
import random


max_x = 30  # this const need to know the max x coordinat
max_y = 30  # this const need to know the max y coordinat


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


class Cell:
    alive = True
    neighbors = []
    live_neightbors = 0

    # this function update live neightbords
    def update_live_neightbord(self):
        self.live_neightbors = 0
        for j in range(len(self.neighbors)):
            if self.neighbors[j].alive:
                self.live_neightbors += 1

    # this function detect die or live this Cell after the move
    def next_die_or_live(self):
        # checking die or live cell(it deepens of number of neighborhoods)
        if self.live_neightbors < 3 or self.live_neightbors > 3:
            self.alive = False
        else:
            self.alive = True


# this function made the strtest field
def init_field():
    # make a array
    array = []
    # making cell in this array
    for i in range(max_y):
        array.append([])
        for j in range(max_x):
            new_cell = Cell()
            new_cell.alive = random.getrandbits(1)
            array[i].append(new_cell)

    # making link to cell in this array
    for i in range(max_y):
        for j in range(max_x):
            array[i][j].neighbors.append(array[(i - 1) % max_y][j])
            array[i][j].neighbors.append(array[(i + 1) % max_y][j])
            array[i][j].neighbors.append(array[i][(j - 1) % max_x])
            array[i][j].neighbors.append(array[i][(j + 1) % max_x])
            array[i][j].neighbors.append(array[(i + 1) % max_y][(j - 1) % max_x])
            array[i][j].neighbors.append(array[(i + 1) % max_y][(j + 1) % max_x])
            array[i][j].neighbors.append(array[(i - 1) % max_y][(j - 1) % max_x])
            array[i][j].neighbors.append(array[(i - 1) % max_y][(j + 1) % max_x])

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

    print(field.field)


if __name__ == '__main__':
    arr = init_field()
    a = Field(arr)
    while True:
        move(a)

