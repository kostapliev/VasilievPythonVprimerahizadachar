tex = input()
text = list(tex)
j=0
for i in range(len(tex)):
    try:
        swap = text[j]
        text[j] = text[j+2]
        text[j+2] = swap
        j+=3
    except:
        continue
print(text)
