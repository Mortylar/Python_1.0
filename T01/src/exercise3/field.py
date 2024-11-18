

class Field:

    def __init__(self, str_list):
        self.__EMPTY = "0"
        self.__FULL = "1"
        self.__real_square = 0
        self.__squares_count = 0
        self.__curcles_count = 0
        self.__field = str_list

    def get(self, i,j):
        return self.__field[i][j]

    def print(self):
        for i in range(len(self.__field)):
            for j in range(len(self.__field[i])):
                print(self.get(i,j), end="")

    def print_figures_count():
        print(self.__squares_count, end=" ")
        print(self.__curcles_count)

    def clear_figure(self, i, j):
        print(i , j)
        if (i < 0) or (i >= len(self.__field)):
            return
        if (j < 0) or (j >= len(self.__field[i])):
            return
        if (self.__field[i][j] == self.__FULL):
            self.__real_square += 1
            self.__field[i][j] = self.__EMPTY
        self.clear_figure(i, j + 1)
        self.clear_figure(i, j - 1)
        self.clear_figure(i + 1, j)
        self.clear_figure(i - 1, j)

    def calculate_deputat_square(self, i, j):
        print(i, j) #TODO
        length = 0
        index = 0
        while self.__field[i][index + j] == self.__FULL:
            print (index, length) #TODO 
            index += 1
            length += 1
        return length * length

    def analyze(self):
        for i in range(len(self.__field)):
            for j in range (len(self.__field[i])):
                if (self.__field[i][j] == self.__FULL):
                    tmp_square = self.calculate_deputat_square(i, j)
                    self.clear_figure(i, j)
                    if (tmp_square == self.__real_square):
                        self.__squares_count += 1
                    else:
                        self.__curcles_count += 1







