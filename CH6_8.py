def functio(a, n, i=1,):
	if n>0:
		return i + functio(a, n-1, i*a)
	else:
		return 0
summ = functio(2, 10, 1)
print(summ)
