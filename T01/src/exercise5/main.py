
def read_float():
    str = input();
    int_part = 0;
    dec_part = 0.0;
    sign = 1;
    ind = 0;
    while ((str[ind] == '+') or (str[ind] == '-')):
        if (str[ind] == '-'):
            sign *= -1;
        ind = ind + 1;
    while (str[ind] != '.'):
        check(str[ind]);
        int_part = 10 * int_part + (ord(str[ind]) - ord("0"));
        ind = ind + 1;
        if (ind >= len(str)):
            return sign * int_part * 1.0;
    for i in range(len(str) - 1, ind, -1):
        if (str[i] == "." or str[i] == "+" or str[i] == "-"):
            raise Exception("Invalid Argument")
        check(str[i]);
        dec_part = dec_part/10 + (ord(str[i]) - ord("0"))/10;

    return sign * (int_part + dec_part);





def check(ch):
    if (ch < '0' or ch > '9'):
        if (ch != '+') and (ch != '-') and (ch != '.'):
            raise Exception("Invalid Argument");



def main():
    try:
        f = 2 * read_float()
        print('%.3f' % f)
    except Exception:
        print("Invalid Argument");

if __name__ == "__main__":
    main();
