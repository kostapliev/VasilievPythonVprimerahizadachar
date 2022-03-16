text = input("Введите текст")

dicti = {}

for i in text:
    if i in dicti.keys():
        continue
    dicti[i] = text.replace(i,"")
print(dicti)
