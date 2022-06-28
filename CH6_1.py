
def functio(a, b):
	summ = 0
	max_iterations = len(a) if len(a)>len(b) else len(b)
	j=0
	for i in range(max_iterations):
		if len(a) > len(b):
			summ += a[i]*b[j]
			j+=1
			if j==len(b):
				j = 0
		else:
			summ += a[j]*b[i]
			j+=1
			if j == len(a):
				j == 0
	return summ
	
a = [1,2,3,4,5,6]
b = [7,8,9,0]

hel = functio(a, b)
print(hel)
			
