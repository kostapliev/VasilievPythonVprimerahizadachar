from random import *

def functi(stro, stolb):
    val = 'A'
    res = [['' for i in range(stro)] for j in range(stolb)]
    for i in range(stolb):
        for j in range(stro):
            res[i][j] = chr(ord(val)+randint(0,23))
    return res
seed(2024)
ex = functi(3,4)

print(ex)