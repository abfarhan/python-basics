

def main():
    x, y = 30, 20

    if (x < y):
        st = "x is less than y"
    elif (x > y):
        st = "x is greater than y"
    else:
        st = "x and y are same"
    
    print(st)

    # conditional statement
    str = "x is less than y" if(x < y) else "x is greater than or equal to y"

    print(str)


if __name__ == '__main__':
    main()