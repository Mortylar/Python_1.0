


class Field:

    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data;
   
    def get_max_count(self):
        return self.__rec_count_max(0, 0)

    def __rec_count_max(self, row, col):
        down = 0
        right = 0
        if (row == self.__rows) or (col == self.__cols):
            return 0
        if (row < self.__rows) and (col < self.__cols):
            right = self.__rec_count_max(row, col + 1) 
            down = self.__rec_count_max(row + 1, col)
            return self.__data[row][col] + max(down, right)


def read_field():
    size = read_line()
    data = []
    for i in range(0, size[0]):
        data.append(read_line())
    field =  Field(size[0], size[1]);
    field.set_data(data);
    return field;


def read_line():
    return list(map(int, input().split(" ")));



def main():
    field = read_field();
    print(field.get_max_count())


if __name__ == "__main__":
    main()
