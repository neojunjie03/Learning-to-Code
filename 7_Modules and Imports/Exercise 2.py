import datetime as dt

today = dt.date.today()
print(today.strftime("%d/%m/%y"))

print(today.strftime("%A"))

christmas = dt.date(2026, 12, 25)
days_left = christmas - today
print(days_left.days)