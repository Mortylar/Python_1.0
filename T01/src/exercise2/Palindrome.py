
def is_palindrome(num):
    if num < 0:
        return False
    if num < 10:
        return True
    divider = 1;
    mirror_number = 0;
    while num > divider:
        mirror_number = mirror_number * 10 + int((num / divider) % 10)
        divider *= 10
    return num == mirror_number

def main():
    print(is_palindrome(int(input())))

if __name__ == "__main__":
    main()


