text = input().split()
print(text)
listofsize = []
for i in text:
    listofsize.append(len(i))
print(listofsize)
print(min(listofsize))
text.pop(listofsize.index(max(listofsize)))
text.pop(listofsize.index(min(listofsize)))

print(text)
