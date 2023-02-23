import re

s = "DosymzhanBaidyrakhman"

result = re.findall(r'[A-Z][^A-Z]*', s)
print(result)
