class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name} {self.age} "
    
    def MyFunc(self):
        print("Hello my name is " + self.name)
        
        
p1 = Person("Dosymzhan" , "18")
p2 = Person("Dosymzhan" , "18")
del p1
# p1.age = 19
# del p1.age
print(p2)
p2.MyFunc()