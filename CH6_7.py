def functio(text):
	print(text[0], end="", sep="")
	if len(text)>2:
		return functio(text[2:])
	
functio("HEELLOe")
