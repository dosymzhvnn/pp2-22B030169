import re
s = "dkan idna.oen  bicnsi,i,o,o,y3, ..9..,k,jj -98 80= ir 93ib"

result = re.sub(r'[,. ]', ':', s)
print(result)