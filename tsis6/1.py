import os
import re
s = os.getcwd()
file = r'C:/Users/dosya/OneDrive/Документы/GitHub/pp2-22B030169/tsis4/generators'

c = ' '.join(os.listdir(file))
pattern = r'.*[.py]'
# print(s)
list = re.findall(pattern , c)
print(list)
