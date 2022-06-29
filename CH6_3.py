def functio(*numbers):
	avsum=0
	for i in numbers:
		avsum+=i
	print("Average: ", avsum/len(numbers), "Maximum: ",max(numbers), "Minimum: ",min(numbers))


functio(1,2,3,4,5,6,7,8,9,0)
