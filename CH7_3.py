chislo = int(input("Введите число"))
string = bin(chislo)
print(string)
summ = 0
for i in string:
    if i=="1":
        summ+=1
print(summ)
