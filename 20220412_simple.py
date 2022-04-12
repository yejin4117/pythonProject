#예약어
import keyword
print(keyword.kwlist)

print('-'*80)
#달력 보기
import calendar
print(calendar.month(2022, 4))
print(calendar.month(2005, 7))
print(calendar.month(2003, 2))
print(calendar.month(1969, 7))

print('-'*80)
#현재 날짜와 시각 보기
import datetime
now = datetime.datetime.now()
print(now)
print(now.year, now.month, now.day, now.hour, now.minute, now.second)
birthday = datetime.datetime(2022, 4, 11)
print(now - birthday)
my_birthday = datetime.datetime(2005, 7 ,15)
print(now - my_birthday)
christmas = datetime.datetime(2022, 12, 25)
print(christmas - now)

print('-'*80)
#윈도우 보기
#import tkinter as tk
#base = tk.Tk()
#base.mainloop()

#turtle
import turtle as t
t.shape('turtle')
t.speed(1)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
#fd = forward
#right = rt
t.rt(144)
t.fd(100)
t.rt(144)
t.fd(100)
t.rt(144)
t.fd(100)
t.rt(144)
t.fd(100)
t.rt(144)
t.fd(100)
t.rt(144)


t.mainloop()

