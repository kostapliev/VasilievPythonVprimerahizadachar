command = input('Введите 1 для первого варианта или 2 для второго')
if command == '1':
    print("Решение первым способом уравнения вида Ax = B - A -1")
    A = int(input('Введите А: '))
    B = int(input('Введите B: '))
    if A != 0:
        x = (B-1)/A-1
        print(x)
    if A == 0 and B == 1:
        print("Любое число решение")
    if A == 0 and B != 1:
        print("Нет решения")
elif command == '2':
    print('Решение вторым способом уравнения вида Ax = B - A -1')
    A = int(input('Введите А: '))
    B = int(input('Введите B: '))
    if A != 0:
        x = (B-1)/A-1
        print(x)
    if A == 0 and B == 1:
        print("Любое число решение")
    try:
        if A == 0 and B != 1:
            raise Exception
    except:
        print("Нет решения") 
else:
    print("Неизвестная команда")