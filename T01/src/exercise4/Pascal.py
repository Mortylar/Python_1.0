
def read_number():
    return int(input())

def print_list(list):
    print(*list, sep=' ')

def print_pascal_line(number):
    if number == 1:
        line = [1]
        print(1)
        return line
    if number == 2:
        line = [1, 1]
        print(1)
        print_list(line)
        return line
    last_line =  print_pascal_line(number - 1)
    line = [1]
    for i in range(len(last_line) - 1):
        line.append(last_line[i] + last_line[i+1])
    line.append(1)
    print_list(line)
    return line




def main():
    try:
        number = read_number()
        print_pascal_line(number)
    except ValueError:
        print('Natural number was expected')


if __name__ == "__main__":
    main();
