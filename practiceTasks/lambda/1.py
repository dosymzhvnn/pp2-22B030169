x = lambda a : a + 15
y = int(input())
print(x(y))

z = int(input())
x = lambda a , b : a * b
print(x(y , z))


x = lambda a , b , c : a + b + c
c = int(input())
print(x(y , z , c))