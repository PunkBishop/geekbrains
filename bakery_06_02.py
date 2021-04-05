from sys import argv


def show_sale():
    with open('bakery.csv', 'r', encoding='utf-8') as base:
        mode = len(argv)
        if mode == 1:
            print(base.read())
        elif mode == 2:
            for line in base.read()[int(argv[1]) - 1:]:
                print(line, end='')
        elif mode == 3:
            for line in base.read()[int(argv[1]) - 1:int(argv[2]) + 2]:
                print(line, end='')


show_sale()
