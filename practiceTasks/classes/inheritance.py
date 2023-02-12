class person:
    def __init__(self , firstname , lastname):
        self.firstname = firstname 
        self.lastname= lastname
        
        
    def printname(self):
        print(self.firstname , self.lastname)
        
        
class student(person):
    def __init__(self , firstname , lastname , year):
        super().__init__(firstname , lastname)
        self.graduationyear = year
        # person.__init__(self , fname , lname)
        
    def welcome(self):
        print("Welcome" , self.firstname , self.lastname ,"to the class of", self.graduationyear)
  
# x = person(FN , LN )
y = student("Dosymzhan", "Baidyrakhman" , "2022")
# x.printname()
# y.printname()
y.welcome()
        