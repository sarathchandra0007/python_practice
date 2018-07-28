class kette(object):
    def __init__(self,name,cost):
        self.name=name
        self.price=cost
        self.on=False
    def switch_on(self):
        self.on=True

sarath=kette('sarath',5)
#dynamic nature
kette.switch_on(sarath)
sarath.power=3
print (sarath.power)
print (sarath.on)

print (kette.__dict__)
"""
print (sarath.on)
print (dir(print))
print (help(print))
"""
