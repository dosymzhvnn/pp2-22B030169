import re

text = "AqhkjlfnjsfniuhLJBJ"
patt = r'^A[a-zA-Z]*J$'
re.findall(patt, text)
print(re.findall(patt, text))