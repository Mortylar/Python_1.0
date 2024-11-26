


class Field:

    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data;

    def print(self):
        for i in range(0, self.__rows):
            for j in range(0, self.__cols):
                print(self.__data[i][j])










def read_field():
    size = read_line()
    data = []
    for i in range(0, size[0]):
        data.append(read_line())
    field =  Field(size[0], size[1]);
    field.set_data(data);
    field.print()
    return field;


def read_line():
    return list(map(int, input().split(" ")));



def main():
    field = read_field();
    print(field.get_data());


if __name__ == "__main__":
    main()
