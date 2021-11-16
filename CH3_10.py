from random import *

lisst = [randint(0,100) for i in range(10)]
lisst1 = [randint(0,100) for i in range(10)]
print(lisst)
print(lisst1)
lisst2 = list()

for i in range(10):
    lisst2.append(lisst[i])
    lisst2.append(lisst1[i])
    
print(lisst2)