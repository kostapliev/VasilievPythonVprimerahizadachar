def functio():
	yield "Понедельник"
	yield "Вторник"
	yield "Среда"
	yield "Четверг"
	yield "Пятница"
	yield "Суббота"
	yield "Воскресенье"

r = functio()

for i in r:
	print(i)
