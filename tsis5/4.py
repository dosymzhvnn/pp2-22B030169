import re
s = "oDosymzhanSHdbhbkjSdjkndcjsouHUIUSSJn"

result = re.findall(r'[A-Z][a-z]+' , s)
print(result)