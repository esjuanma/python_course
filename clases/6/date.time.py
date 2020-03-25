import datetime
from datetime import date, time, timedelta
#import time

#print(type(time))
#print(type(otroTime))

# Now y today
datetime_object = datetime.datetime.now()
date_object = datetime.date.today()

# Diferencia entre now y today (el 2do no tiene hora)
print(datetime_object)
print(date_object)
print('')

# Todos los atributos y métodos de datetime
print(dir(datetime.datetime))
print('')

# 13/04/19
d = datetime.date(2019, 4, 13)
print(d)

# 1326244364 milisegundos desde el 1/1/1970
timestamp = datetime.date.fromtimestamp(1326244364)
print("Date:", str(timestamp)) # 2012-01-11

# date object of today's date
today = datetime.date.today() 
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

# time(hour = 0, minute = 0, second = 0)
a = datetime.time(23)
print("a =", a)

# parametros desordenados
c = time(minute = 34, second = 56, hour = 11)
print("c =", c)

# microsegundos!
a = time(11, 34, 56, 1000)
# print('Anda a encontrarlo', a.time())
print("hour =", a.hour)
print("minute =", a.minute)
print("second =", a.second)
print("microsecond =", a.microsecond)

# diferencia entre fechas
t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print("t1 =", t1)
print("t3 =", t3)

# Qué edad tengo
t1 = date(year = 1991, month = 11, day = 30)
t2 = date.today()
t3 = abs(t1 - t2)
print("t1 =", t1)
print("t3 =", t3)
print("type t3 =", type(t3))
print('')
print(dir(t3))
print('')
print(dir(datetime.timedelta))
print(t3.days / 365, 'años')

# Timedelta
t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2
print("timedelta", t3)


##
# Formateo de fechas!
##
# current date and time
now = datetime.datetime.now()

t = now.strftime("%H:%M:%S %z %Z %j")
print("time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)
