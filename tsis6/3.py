import re

text = '2898'
s = re.findall(r'[0-9]' , text)

print(len(s))



