import datetime

td = datetime.date.today()
s = datetime.timedelta(days = 1)

print("Yesterday :" , td - s , end="\n") 
print("Today :" , td , end="\n")
print("Tomorrow :" , td + s)