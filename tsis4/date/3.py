import datetime

date = datetime.datetime.now()
date1 = date.replace(microsecond=0)
print(date)
print(date1)