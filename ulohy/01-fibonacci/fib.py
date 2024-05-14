def fibrek(n):
    return n if n <= 1 else fibrek(n - 1) + fibrek(n - 2)


def fib(n):
    if n <= 1:
        return n
    prev, fib = 0, 1
    for _ in range(2, n + 1):
        fib, prev = fib + prev, fib
    return fib


n = 35
print("Nerekurzivní řešení:\t", fib(n))
print("Rekurzivní řešení:\t", fibrek(n))
