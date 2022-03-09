chi = int(input())
if chi > 0:
    spisok = []
    for i in range(1,chi+1):
        spisok.append(i)
    
    dicti = {spisok[i]:spisok[-i] for i in range(len(spisok))}

print(dicti)
    
