import time

def f(n):
    for i in range(n+1):
        if i <= n:
            yield i
        
n = int(input())
for i in f(n):
    print(i)
    time.sleep(0.1)