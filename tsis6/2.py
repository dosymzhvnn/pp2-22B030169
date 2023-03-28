def f():
    x = 5
    while True:
            yield x
            x += 5
        

while True:
    s = input()  
    if s == 'next':
        print(next(f()))
print(s)
    