text1 = input("Text 1 ")
text2 = input("Text 2 ")

spisok = []
mayak = 0
ind1 = 0
ind2 = 0
for i in range(len(text1)+len(text2)):
    if mayak == 0:
        try:
            spisok.append(text1[ind1])
        except IndexError:
            spisok.append("*")
        ind1+=1
        mayak+=1
    elif mayak == 1:
        try:
            spisok.append(text2[ind2])
        except IndexError:
            spisok.append("*")
        ind2+=1
        mayak-=1
print(str(spisok))
