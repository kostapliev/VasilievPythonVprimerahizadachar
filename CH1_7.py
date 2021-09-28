ch = int(input("Введите число"))
if ch>0:
    um = 1
    while ch>0:
        um = um * ch
        ch = ch - 1
    print(um)
else:
    print('Вводите положительные числа')