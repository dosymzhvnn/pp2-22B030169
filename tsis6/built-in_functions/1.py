import functools

list = [3 , 4 , 2 , 8]

def multiply(x , y):
    return x * y
result = functools.reduce(multiply,list)
print(result)