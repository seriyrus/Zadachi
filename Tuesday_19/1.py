def delete_vowels(line: str):
    l = list(line)
    for i in l:
        if i in ['a','e','o','i','y','u']:
            l.remove(i)
    x = ''
    for el in l:
        x+=el
    return x

line = "Hello world"
for word in line.split():
    print(delete_vowels(word))
