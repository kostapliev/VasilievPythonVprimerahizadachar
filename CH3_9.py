from random import * 

lisst = [randint(0,99) for i in range(10)]
print(lisst)
lisst_new = list()

for i in range(9):
    lisst_new.append(lisst[i]+lisst[i+1])
    
print(lisst_new)
j = 1
for i in range(9):
    lisst.insert(j, lisst_new[i])
    j+=2
    
print(lisst)