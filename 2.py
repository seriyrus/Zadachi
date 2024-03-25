n = int(input())

votes = list(map(int, input().split()))

votes_list = {}

for i in set(votes):
    votes_list[i] = votes.count(i)

print(votes_list,votes_list.get(1))#max(votes_list.values()))


def search_max(lst):
    try:
        if lst.get(max(lst.values())) <= n:
            return lst.get(max(lst.values()))
        else:
            del votes[lst.get(max(lst.values()))]
            search_max(lst)
    except:
        return lst

print(search_max(votes_list))