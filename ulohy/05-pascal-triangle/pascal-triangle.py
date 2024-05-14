def pascal_triangle(h: int):
    for i in range(1, h + 1):
        print("  " * (h - i), end="")
        for j in range(1, i + 1):
            print("{0:03d} ".format(int(n_over_k(i - 1, j - 1))), end="")
        print()


def fact(n: int)->int:
    if n <= 1:
        return 1
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

def n_over_k(n:int, k:int)->int:
    if n>=k and k>=0:
        return fact(n) / (fact(k) * fact(n-k))
    return 0

pascal_triangle(10)