spisok1 = [1, 2, 4, 5]
spisok2 = [1, 2, 4, 5]

if len(spisok1) == len(spisok2):
    ind = 0
    for i in spisok1:
        if i != spisok2[ind]:
            print("Не равны!")
            break

        if ind==len(spisok2)-1:
            print("Равны")
            break
        ind += 1
else:
    print("Не равны")
