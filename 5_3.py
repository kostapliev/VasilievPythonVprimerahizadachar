text = input("Введите текст на английском")

text2 = ""

for i in text:
    if 65<=ord(i)<=90:
        text2+=chr(ord(i)+32)
    elif 97<=ord(i)<=122:
        text2+=chr(ord(i)-32)
print(text2)
