def is_prime(n):
    prime = n > 1 and (n%2 != 0 or n == 2) and (n%3 != 0 or n == 3)
    i = 5
    d = 2

    while prime and i * i <= n:
        prime =n %i != 0
        i+=d
        d = 6-d
    return prime


def is_hyper_prime(n):
    if is_prime(n):
        while len(str(n)) > 1 and is_prime(n):
            n=n//10
        return True
    return False

print(is_hyper_prime(29399))    