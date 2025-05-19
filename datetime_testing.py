from datetime import datetime, date, time
"""alarm = time(7, 30, 25)
print(alarm.strftime('%H'))
print(alarm.strftime('%M'))
print(alarm.strftime('%S'))"""
"""
birthday = date(1992, 10, 6)
print(birthday.strftime('%B'))
print(birthday.strftime('%A'))
print(birthday.strftime('%Y'))
print(birthday.strftime('%m'))
print(birthday.strftime('%d'))"""

dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11), date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]


for i in dates:
    print(f'{i.year} - Q{(i.month-1)//3+1}')