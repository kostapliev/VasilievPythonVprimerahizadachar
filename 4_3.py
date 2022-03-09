sets = {"а", "и", "е", "ё", "о", "у", "ы", "э", "ю", "я"}

text = input("Введите текст")

for i in text:
    if i in sets:
        print("Найдена гласная буква "+i)
