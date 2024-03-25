def is_prime(number: int):
    l = [2,3,4,5,6,7,8,9,10]
    l.remove(number)
    for n in l:
        if number%n == 0:
            return False
    return True

for i in range(2,11):
    if is_prime(i):
        print(i, end = ' ')
print()