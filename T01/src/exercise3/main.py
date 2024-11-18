import sys
import field

def read_field():
    return map(list, sys.stdin.readlines())

def main():
    s21_field = field.Field(read_field())
    #s21_field.print()
    s21_field.analyze()
    s21_field.print_figures_count()


if __name__ == "__main__":
    main();
