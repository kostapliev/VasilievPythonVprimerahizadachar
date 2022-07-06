from datetime import datetime, date, time
inp = eval(input("Через запятую часы минуты и секунды"))
print(type(inp))
exitt = time(inp[0], inp[1], inp[2])
enter = datetime.now().time()
delta = datetime.combine(date.today(), exitt) - datetime.combine(date.today(), enter)
print(delta)
