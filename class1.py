class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def displayData(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
    
    def addAge(self):
        self.age = self.age + 1

class Dancer(Student):
    def __init__(self, name, age):
        super().__init__(name, age)

    def displayDancerData(self):
        print("Name: ",self.name)

