
from datetime import datetime
date1 = input("Введите дату и время в формате ГОД-МЕСЯЦ-ЧИСЛО ЧАС:МИНУТА:СЕКУНДА")
date2 = input("Введите дату и время в формате ГОД-МЕСЯЦ-ЧИСЛО ЧАС:МИНУТА:СЕКУНДА")

date10 = datetime.fromisoformat(date1)
date20 = datetime.fromisoformat(date2)

interval = date10-date20

print(interval.days)
