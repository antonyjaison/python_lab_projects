class MySampleClass:
    def hello(self,n):
        self.name = n
    def printName(self):
        print(self.name)

x = MySampleClass()
y = MySampleClass()

name = "Antony"

x.hello(name)
y.hello('mariya')
x.printName()
y.printName()