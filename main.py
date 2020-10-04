max_x=1920 # this const need to know the max x coordinat
max_y=1080 # this const need to know the max y coordinat


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


# this functioon is making a move
def move(field):
    field_array = field.get_field()
    new_field_array = []
    for i in range(len(field_array)):
        new_field_array.append([])
        for j in range(len(field_array[i])):
            new_field_array[i].append(field_array[i][j])
    return new_field_array


arr = [[1,2,3], [1,2,3]]
a = Field(arr)
print(move(a))