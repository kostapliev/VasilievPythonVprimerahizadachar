def functio(lister):
	listNew = []
	for i in lister:
		if i%2!=0:
			listNew.append(i)
	return listNew
	
lister = [1,2,3,4,5,6,7,8,9,0]

hey = functio(lister)
print(hey)
