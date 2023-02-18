def evens(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
            
            
n = int(input())
for i in evens(n):
    print(i)
