n,m = map(int,input().split())

_input = []
_output = []

for row in range(n):
    _input.append([el for el in map(int, input().split())])


sr = 0

for row in _input:
    for el in row:
        sr += el

sr = sr / (n * m) 

for row in _input:
    _output.append([0 if el < sr else 255 for el in row])


print(_output)