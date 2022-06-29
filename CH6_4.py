def functio(mytext, *a):
	newtext = ""
	for i in a:
		if i in range(len(mytext)-1):
			newtext += mytext[i]
	return newtext

hey = functio("HELLO my dear", 2, 6, 8, 9)
print(hey)
