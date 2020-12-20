# ошибка в том что соседи увеличиваюиться
import random
from pprint import pprint as pp
import copy
import musicalbeeps
import asyncio

notes = {
    0: "pause",
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E",
    6: "F",
    7: "G",
}

player = musicalbeeps.Player(volume = 0.3,
                            mute_output = False)

mode = "normal"

max_x = 10  # this const need to know the max x coordinat
max_y = 10  # this const need to know the max y coordinat

music_mode = "guitar"


def num_to_binary_system(n):
    b = []

    while n > 0:
        b.append(n % 2)
        n = n // 2

    for i in range(len(b) - 1, max_x * max_y):
        b.append(0)

    return b


# this class need to save the position of field
class Field:
    def __init__(self, array):
        self.field = array
        self.changes = []
        self.iteration = -1
        self.music_bits = []

    # this function change the field
    def change_field(self, array):
        self.field = array

    # this funcition is returned field as array
    def get_field(self):
        return self.field

    # this function is making a move(i + 1) % max_y
    def move(self):
        if self.iteration >= len(self.changes) - 1:
            self.changes.append([])

            # there we update live neighbords in all cell
            for i in range(len(self.field)):
                for j in range(len(self.field[i])):
                    self.field[i][j].update_live_neightbord()

            # there we kill or make new cell
            for i in range(len(self.field)):
                for j in range(len(self.field[i])):
                    old_stateu = self.field[i][j].alive

                    self.field[i][j].next_die_or_live()

                    if(old_stateu != self.field[i][j].alive):
                        print('yeeeeeee')
                        self.changes[-1].append((i, j))

            self.iteration = len(self.changes) - 1
        else:
            self.iteration += 1

            for coord in self.changes[self.iteration]:
                self.field[coord[0]][coord[1]].alive = not self.field[coord[0]][coord[1]].alive

    def previous(self):
        array = []

        print("nice")

        for i in range(2 ** (max_x * max_y)):
            bits = num_to_binary_system(i)
            field_1 = Field(init_field())
            for j in range(max_x):
                for k in range(max_y):
                    coord = max_y * j + k

                    field_1.field[k][j].alive = bool(bits[coord])

            print(i)

            pred = copy.deepcopy(field_1.field)
            #pp(pred)

            field_1.move()

            if (self.field == field_1.field):
                #pp(array)
                array.append(pred)

        if (len(array) > 0):
            print('ggggg')
            pp(array)
            self.field = array[0]

    def prev(self):
        if (self.iteration > 0):
            for coord in self.changes[self.iteration]:
                self.field[coord[0]][coord[1]].alive = not self.field[coord[0]][coord[1]].alive

            self.iteration -= 1

    def make_bits(self, field):
        stroka = ""

        for element in field:

            for bit in element:
                stroka += str(int(bit.alive))

        for i in range(0, len(stroka), 3):
            stroka_1 = ""

            try:
                stroka_1 += stroka[i]
                stroka_1 += stroka[i+1]
                stroka_1 += stroka[i+2]

                self.music_bits.append(stroka_1)
            except:
                pass

    def make_music_bits(self):
        self.make_bits(self.field)

        return self.music_bits

    def make_music(self):
        sound = self.make_music_bits()

        return sound


class Bits:
    def make_bit_dec(self, bit):
        dec = 0

        for i in range(len(bit)):
            dec += int(bit[i]) * (2**i)

        if dec > 7:
            print(bit)

        return dec



class Sound:
    async def make_sound(self, sound):
        for element in sound:
            if(mode == "normal"):
                print("FUCk")
                sound = notes[Bits.make_bit_dec(self, element)]
                player.play_note(sound, 1.0)
                await asyncio.sleep(1)
            else:
                pass

class Cell:
    alive = True
    live_neightbors = 0

    def __init__(self):
        self.neighbors = []

    def __eq__(self, other):
        return self.alive == other.alive

    def __repr__(self):
        return str(self.alive)

    # this function update live neightbords
    def update_live_neightbord(self):
        self.live_neightbors = 0

        for j in range(len(self.neighbors)):
            if self.neighbors[j].alive:
                self.live_neightbors += 1

    # this function detect die or live this Cell after the move
    def next_die_or_live(self):
        if mode == "normal":
            # checking die or live cell(it deepens of number of neighborhoods)
            if (self.live_neightbors < 2 or self.live_neightbors > 3) and self.alive == True:
                self.alive = False
            elif self.live_neightbors < 2 or self.live_neightbors > 3:
                self.alive = False
            elif self.live_neightbors == 2 and self.alive == False:
                self.alive = False
            else:
                self.alive = True

        else:
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


def app(xs):
    xs[0] = 2


if __name__ == '__main__':
    # arr = init_field()
    # a = Field(arr)
    # while True:
    #     move(a)
    # print(num_to_binary_system(6))
    # xs = [1, 2]
    # app(xs)
    # print(xs)
    ...