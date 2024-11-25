import sys
import field

def read_field():
    str = sys.stdin.readlines()
    return list(map(list, [i.replace(" ", "") for i in str]))

def main():
    s21_field = field.Field(read_field())
    s21_field.analyze()
    s21_field.print_figures_count()


if __name__ == "__main__":
    main();
