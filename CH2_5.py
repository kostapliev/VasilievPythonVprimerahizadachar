var = eval(input())
verh = int(input("Введите верхнюю сумму"))
summ = 0
for i in range(verh+1):
    if i in var:
        continue
    summ += i
print(summ)