from atexit import register


def f(*args, **kwargs):
    data = args
    new_data = []
    try:
        to_sort = kwargs["to_sort"] and type(kwargs["to_sort"]) == bool
    except:
        to_sort=False
    try:
        step = kwargs["step"]
    except:
        step=1

    try:
        register = kwargs["register"]
    except:
        register = None

    for el in data:

        el = list(el)
        el.reverse()
        el = ''.join(el)


        s=''
        for letter in range(0, len(el), step):
            s+=el[letter]

        s=list(s)
        s=''.join(s)

        if register == 0:
            s=s.lower()
        if register == 1:
            s=s.upper()
        if register == 2:
            s = s[0].upper() + s[1:]
        else:
            s = s[0].upper() + s[1:].lower()

        new_data.append(s)
        

    if to_sort:
        return sorted(new_data)
    
    return new_data

data = ['once', 'there', 'large', 'caravan', 'going', 'through', 'desert']

data = f(*data, register=4,step=2, to_sort=True)
print(*data)