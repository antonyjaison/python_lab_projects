class MySampleClass():
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
    
    def add_age(self):
        self.age = self.age + 1
    
    def relocate(self,place):
        self.place = place

x = MySampleClass("Antony",19,"Angamaly")
y = MySampleClass("Ann Mariya",15,'Ernakulam')

x.add_age()
y.add_age()