chi = int(input())
lists = [ 1 for k in range(chi)]

n = 0
i = 0
while i<chi:
    if n % 2 != 0:
        lists[i] = n
        i = i + 1
    n = n + 1
print(sum(lists))