#Create a class person with an initial age that must be above 0, allows yearly passage of time incrementing age, and
#print where the instance of the class is located on the spectrum of adulthood

class Person:
    def __init__(self,initialAge):
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            initialAge=0
            self.age = initialAge
        else:
            self.age = initialAge     
        return None
    
    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age <18:
            print("You are a teenager.")
        else:
            print("You are old.")
        return None           
        
    def yearPasses(self):
        self.age+=1
        return self.age


# Testing Logic - Works
t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
