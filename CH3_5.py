from random import *

res = [[randint(0,10) for i in range(5)] for j in range(5)]
print(res)

strok = int(input())
stolb = int(input())

i=0
while i<5:
    res[strok].pop()
    i+=1

i = 0

print(res)
while i<5:
    try:
        del res[i][stolb]
    except IndexError:
        print("error")
    i+=1
    
print(res)