from datetime import datetime, date, timedelta


now = datetime.now()
today = date.today()

showAll = datetime.now().strftime('%Y/%m/%d %H:%M:%S.%f %A %a %B %b')
print(showAll)
baseDate = date(2023, 4, 1)
days = timedelta(days=1)
weeks = timedelta(weeks=2)
hours = timedelta(hours=1)
minutes = timedelta(minutes=1)

l = [(baseDate + i * days).strftime('%Y/%m/%d') for i in range(4)]