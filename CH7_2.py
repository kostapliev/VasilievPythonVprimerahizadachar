chislo = int(input("Ввожу целое число: "))
bit = int(input("Номер бита: "))

stri=bin(chislo)[2:]
print(stri[bit])
