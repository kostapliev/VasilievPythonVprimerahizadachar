from fractions import Fraction
int1 = eval(input("Введите через запятую числитель и знаменатель"))
A = Fraction(int1[0], int1[1])
int2 = eval(input("Введите через запятую числитель и знаменатель"))
B = Fraction(int2[0], int2[1])
set1 = set()
A1 = A+B
set1.add(A1)
A2 = A-B
set1.add(A2)
A3 = A*B
set1.add(A3)
A4 = A/B
set1.add(A4)
print(set1)
print("Min ", min(set1))
print("Max ", max(set1))
