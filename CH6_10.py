def functio(n):
	for i in range(n):
		yield i**2

step = functio(10)

print(list(step))
	
