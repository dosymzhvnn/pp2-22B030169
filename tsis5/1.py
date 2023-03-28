import re

a = "aa0dipoufuuuabbbbbbbbd bdduwabbb"
result = re.findall(r'([a][{b}]*)', a)
print(result)