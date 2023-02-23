import re

a = "a0dipoufuuuabbbbbbbbd bdduwabbb"
result = re.findall(r'([a]+[{b}]*)|[a]', a)
print(result)