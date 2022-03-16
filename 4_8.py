dicti = {}

for i in range(3):
    name = input("Введите фамилию автора ")
    proiz = input("Введите название произведения ")
    dicti[name] = proiz

prav = 0
neprav = 0
for i in dicti.keys():
    print("Кто написал", dicti[i])
    text = input()
    if text == i:
        print("Молодец!")
        prav += 1
    else:
        print("учись по бр")
        neprav += 1

print("Всего правильных ответов", prav)
print("Всего неправильных ответов", neprav)

