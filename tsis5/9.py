import re

def insert_spaces(s):
    pattern = r'(?<=\w)([A-Z])'
    return re.sub(pattern, r' \1' , s)

s = "MyNameIsDosymzhan.ILovePython!"
s_with_spaces = insert_spaces(s)
print(s_with_spaces)