def is_prime_number(n: int) -> bool:
    for i in range(2, n, 1):
        if n % i == 0:
            return False
    return True


n = 1
prime_number_counter = 0
while prime_number_counter < 20:
    n += 1
    if is_prime_number(n):
        prime_number_counter += 1
        print(f"{prime_number_counter:2}. {n}")
