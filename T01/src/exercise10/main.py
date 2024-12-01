class Apparat:

    def __init__(self, list):
        self.YEAR = 0
        self.PRICE = 1
        self.TIME = 2
        self.__data = list

    def print(self):
        print(self.__data)

    def get_year(self):
        return self.__data[self.YEAR]

    def get_price(self):
        return self.__data[self.PRICE]

    def get_time(self):
        return self.__data[self.TIME]

class ApparatList:

    def __init__(self, apparat):
        self.__year_key = apparat.get_year()
        self.__data = [apparat]

    def print(self):
        for ap in self.__data:
            ap.print()

    def get_key(self):
        return self.__year_key

    def add_apparat(self, apparat):
        if (self.__year_key == apparat.get_year()):
            self.__data.append(apparat)
            return True
        return False

    def count_min_price_by_time(time):
        price = -1
        for i in range(0, len(self.__data)):
            for j in range(i + 1, len(self.__data)):
                if (self.__data[i].get_time() + self.data[j].get_time() >= time):
                    tmp_price = self.__data[i].get_price() + self.__data[j].get_price()
                    if (tmp_price > price):
                        price = tmp_price
        return price

class ApparatsService:

    def __init__(self):
        self.__count = 0
        self.__total_time = 0
        self.__apparats = []

    def add_apparat(self, apparat):
        for i in range(0, len(self.__apparats)):
            if (self.__apparats[i].add_apparat(apparat)):
                return
        self.__apparats.append(ApparatList(apparat))
        return

    def __read_header(self):
        header_list = input().split(" ")
        self.__count = (int)(header_list[0])
        self.__total_time = (int)(header_list[1])

    def read(self):
        self.__read_header()
        for i in range(0, self.__count):
            self.add_apparat(Apparat(list(map(int, input().split(" ")))))
        print(self.__count)
        print(self.__total_time)
        for a in self.__apparats:
            a.print()

def main():
    ap = ApparatsService()
    ap.read()

if __name__ == "__main__":
    main()
