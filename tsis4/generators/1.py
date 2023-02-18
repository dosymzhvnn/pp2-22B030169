import math
def n_square(n):
    for i in range(n):
        if i <= n:
            yield i * i
        else:
            break
    
n = int(input())
for i in n_square(n):
    print(i)