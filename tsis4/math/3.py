import math

n = int(input())
l = int(input())
perimetr = l * n
a = (l / (2 * math.tan(math.pi / n)))
f = a * perimetr
print(int(f / 2))