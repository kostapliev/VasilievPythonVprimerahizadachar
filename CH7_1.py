osnovanie = int(input("Введите основание для системы счисления: "))
chislo = int(input("Теперь введите само число: "))

if osnovanie == 2:
    print(bin(chislo))
elif osnovanie == 8:
    print(oct(chislo))
elif osnovanie == 16:
    print(hex(chislo))
else:
    print("Не могу в такое основание (")
