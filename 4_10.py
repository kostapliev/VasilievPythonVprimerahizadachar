dicti1 = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7}
dicti2 = { "5":5, "6":6, "7":7, "8":8, "9":9}

set1 = set()
set2 = set()

for i in dicti1.keys():
    set1.add(i)
for i in dicti2.keys():
    set2.add(i)
dicti3 = {}

set3 = set1&set2

for i in set3:
    dicti3[i] = set([dicti1[i], dicti2[i]])
print(dicti3)
