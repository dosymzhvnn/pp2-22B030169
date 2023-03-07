def f(str):
    d = {"upper": 0 , "lower" : 0}
    for letter in str:
            if letter.isupper():
                d["upper"] += 1
            else:
                d["lower"] += 1
    print("Upper_case letters :", d["upper"])
    print("Lower_case letters :", d["lower"])
    
s = input()  
f(s)