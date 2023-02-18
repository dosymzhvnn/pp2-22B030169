def squares(a , b):
    for i in range(b+1):
        if i >= a and i <= b:
            yield i * i
            
            
a = int(input())
b = int(input())
for i in f(a , b):
    print(i)