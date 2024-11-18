from array import *

def read_number():
    return int(input())


def main():
    try:
        number = read_number()
        print(number)
    except ValueError:
        print('Natural number was expected')


if __name__ == "__main__":
    main();
