dliny = eval(input("Введите длины трех сторон: "))

if (dliny[0] <= (dliny[2] + dliny[1])) or (dliny[1] <= (dliny[0] + dliny[2])) or (dliny[2] <= (dliny[0] + dliny[1])):
        print("Не существует")
else:
    print('существует')
    