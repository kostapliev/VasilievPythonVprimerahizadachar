filename = input("Введите название файла")
pred= "NEW FILE\n"
with open(filename) as fn:
    k = 1
    cop = open("copy.txt", 'w+t')
    for L in fn:
        cop = open("copy.txt", "a")
        pred = "["+str(k)+"]"+L
        cop.write(pred)
        cop.close()
        k+=1
    cop = open("copy.txt", 'r')
    print(cop.read())
    
        
