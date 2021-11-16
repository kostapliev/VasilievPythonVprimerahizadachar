s = input("Введите текст: ")
ts = tuple(s)
step = int(input('введите шаг '))
lists = []
g=0 # для подсчета шага
i=0 # для подсчета строки
while i < len(s):
    if g<len(s):
        lists.append(s[g])
    g += step
    i += 1
ts1 = tuple(lists)
print(ts1)