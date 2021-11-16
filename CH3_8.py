from random import *

lisst = [randint(0,99) for i in range(10)]
print(lisst)

for i in range(10):
    for j in range(10-i-1):
        if j+2<=9 and j%2==0 and lisst[j] > lisst[j+2]:
            lisst[j], lisst[j+2] = lisst[j+2], lisst[j]
        if j+2<=9 and j % 2 != 0 and lisst[j] < lisst[j+2]:
            lisst[j], lisst[j+2] = lisst[j+2], lisst[j]
            
print(lisst)