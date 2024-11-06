

def scalar_product(first, second):
    result = 0;
    for i in range(3):
        result += first[i] * second[i]
    return result


def read_vector():
    str_vector = input().split(" ");
    return list(map(float, str_vector))

def print_number(number):
    print(number)
    
def main_service():
    x = read_vector()
    y = read_vector()
    print_number(scalar_product(x, y))

def main():
    main_service()
#    read_vector()

if __name__ == "__main__":
    main()
