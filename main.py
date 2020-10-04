# в ходе должнобыть вычисление соседедей у каждой клетки потом уюийсвто и ли оставление в живых рождение
# сделать ссылки на соседей
import random


max_x = 100  # this const need to know the max x coordinat
max_y = 100  # this const need to know the max y coordinat


# this class need to save the position of field
class Field:
    def __init__(self, array):
        self.__field = array

    # this function change the field
    def change_field(self, array):
        self.__field = array

    # this funcition is returned field as array
    def get_field(self):
        return self.__field


class Cell:
    alive = True
    neighbors = []
    live_neightbors = 0

    # this function update live neightbords
    def update_live_neightbord(self):
        self.live_neightbors = 0
        for i in range(len(self.live_neightbors)):
            for j in range(len(self.neighbors[i])):
                if self.live_neightbors.alive:
                    self.live_neightbors += 1

    # this function detect die or live this Cell after the move
    def next_die_or_live(self):
        return self.alive

# this function made the strtest field
def init_field():
    array = []
    for i in range(max_y):
        array.append([])
        for j in range(max_y):
            new_cell = Cell()
            new_cell.alive = random.getrandbits(1)
            array[i].append(new_cell)

    return array


# this function is making a move
# def move(field):
    # field_array = field.get_field()
    # new_field_array = []
    # for i in range(len(field_array)):
    #     new_field_array.append([])
    #     for j in range(len(field_array[i])):
    #         print(i, j, field_array[i][j].die_or_live())
    # return new_field_array


if __name__ == '__main__':
    arr = init_field()
    a = Field(arr)
    #move(a)