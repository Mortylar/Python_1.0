

def read_int():
    return int(input())

def count_uniq_numbers():
    number_count = read_int()
    num_set = set()
    for i in range (0, number_count):
        num_set.add(input())
    return len(num_set)




def main():
    print(count_uniq_numbers())

if __name__ == "__main__":
    main()
