dliny = eval(input("Введите длины трех сторон: "))

if (dliny[0] < (dliny[2] + dliny[1])) and (dliny[1] < (dliny[0] + dliny[2])) and (dliny[2] < (dliny[0] + dliny[1])):
    print("существует")
else:
    print('Не  существует')
