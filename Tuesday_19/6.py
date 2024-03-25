n = int(input()) 
m = int(input())


def ReduceFraction(n, m):
    smaller = n
    nod = []
    if n > m:
        smaller = m
    if n == m:
        print("1 1")
        return
    else:
        for i in range(1, smaller):
            if n%i == 0 and m%i == 0:
                nod.append(i)

    print(f"{n//max(nod)} {m//max(nod)}")

ReduceFraction(n, m)