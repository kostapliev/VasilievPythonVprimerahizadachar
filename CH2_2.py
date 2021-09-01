chislo = input("Введите число: ")
s = ""
for i in chislo:
    if i == "9":
        s = s + "0"
    elif i == "8":
        s = s + "1"
    elif i =='7':
        s = s + '2'
    elif i == '6':
        s = s + '3'
    elif i == '5':
        s = s + '4'
    elif i == '4':
        s = s + '5'
    elif i == '3':
        s = s + '6'
    elif i == '2':
        s = s + '7'
    elif i == '1':
        s = s + '8'
print(s)