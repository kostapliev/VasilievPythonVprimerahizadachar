text = input("enter the text")

sets = set(text)

spisok = list(sets)

dicti = {spisok[i]:0 for i in range(len(spisok))}

for i in text:
    if i in dicti.keys():
        dicti[i]+=1

print(dicti)
