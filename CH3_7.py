from random import *

lis = [randint(0,9) for i in range(10)]

def functio(lis):
    li=list()
    li.append(max(lis))
    li.append(lis.index(max(lis)))
    
    return li


es = functio(lis)

print(lis)
print(es)
    