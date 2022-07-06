fn = input("Введите имя файла: ")
txt = input("Введите текст для записи: ")
with open(fn, "w") as fin:
    fin.write(txt.upper())
print("Конец файла")
