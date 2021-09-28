ch = int(input())

lists = [1 for k in range(ch)]

n = 2
lists[0] = 1
lists[1] = 1
while n<ch:
    lists[n] = lists[n-1] + lists[n-2]
    n = n + 1
print(lists)