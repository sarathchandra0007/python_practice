class Car():
    def __init__(self,name):
        self.name=name
    def muname(self):
        print ("sarath")
class Specific(Car):

    def __init__(self,name,type):
        Car.__init__(self,name)
        self.type=type
    def printcar(self):
        print ("Car is {} and type is {}".format(self.name,self.type))

s=Specific("Toyota","4wheel")
s.printcar()
s.muname()
