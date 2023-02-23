import re
s = "dkanidnaoienbicnsiijooa390kjj-9880=ir93ib"

result = re.findall(r'[a].+b$' , s)
print(result)