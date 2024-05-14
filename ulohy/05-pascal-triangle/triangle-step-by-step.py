def triangle_1(h):
    for i in range(1, h + 1):
        print("A" * i)


def triangle_2(h):
    for i in range(1, h + 1):
        print("A" * (i * 2 - 1))


def triangle_3(h):
    for i in range(1, h + 1):
        print(" " * (h - i), end="")
        print("A" * (i * 2 - 1))


def triangle_4(h):
    for i in range(1, h + 1):
        print("  " * (h - i), end="")
        for j in range(0, i):
            print("000 ", end="")
        print()


def triangle_5(h):
    for i in range(1, h + 1):
        print("  " * (h - i), end="")
        for j in range(0, i):
            print("{0:03d} ".format(i), end="")
        print()



triangle_1(4)
triangle_2(4)
triangle_3(4)
triangle_4(4)
triangle_5(4)
