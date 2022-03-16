text = input("")
text2 = ""
for i in text:
    if 65<=ord(i)<=89 or 97<=ord(i)<=121:
        text2+=chr(ord(i)+1)
    elif ord(i)==90:
        text2+=chr(65)
    elif ord(i)==122:
        text2+=chr(97)
    else:
        text2+=i
print(text2)
