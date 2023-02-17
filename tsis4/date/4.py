import datetime

d1 = str(input())
d2 = str(input())
d11 = datetime.datetime.strptime(d1 ,'%Y %m %d')
d22 = datetime.datetime.strptime(d2 ,'%Y %m %d')
time_diff = d22 - d11
tsecs = time_diff.total_seconds()
print(tsecs)