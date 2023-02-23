import re

s = 'ljcnkbcsiuaiuakjadbabbaaabbababababbbabdkljljdeuf'

result = re.findall(r'[a][b]{2,3}+' , s)

print(result)