n = int(input())

list_ = map(str, input().split())

print(list_)

deystvia = {'R':"read", 'W':"write", 'X':"execute"}

prava = {}

for i in range(n):
    prava[list(map(str, input().split()))[0]] = [list(map(str, input().split())).pop[0]]

print(prava)