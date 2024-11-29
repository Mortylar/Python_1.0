
class Polly:

    def __init__(self):
        self.__point = 0.0
        self.__power = 0
        self.__data = []

    def diff(self):
        diff = Polly();
        diff.__point = self.__point;
        diff.__power = self.__power - 1;
        for i in range(0, self.__power):
            diff.__data.append((self.__power - i) * self.__data[i])
        return diff

    def get_value(self):
        result = 0.0
        for i in range(0, 1 + self.__power):
            result = result + self.__data[i] * (pow(self.__point, self.__power - i))
        return result

    def read_header(self):
        header = input().split(" ");
        self.__power = (int)(header[0])
        self.__point = (float)(header[1])

    def read_polly(self):
        self.read_header(); 
        for i in range(0, self.__power + 1):
            self.__data.append((float)(input()))


def main():
    polly = Polly()
    polly.read_polly()
    print('%.3f' % polly.diff().get_value())

if __name__ == "__main__":
    main()
