def factorization(number:int ):
    fac=''
    while number != 1:
        for i in [2,3,5,7,9]:
            if number % i == 0:
                fac+=str(i)
                number = number / i
    l = sorted([n for n in fac])
    text = ''
    for el in set(l):
        if l.count(el) != 1:
            text+=str(el) + "^" + str(l.count(el)) + '*'
        else:
            text+=str(el) + '*'

    print(text[:-1])



factorization(360)
factorization(75)
factorization(5)

