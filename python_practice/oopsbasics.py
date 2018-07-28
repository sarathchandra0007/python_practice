
class Dog():
    species="mammal"

    def __init__(self,breed,name):
        self.breed=breed
        self.name=name

mydog=Dog("Lab","Sammy")

print (mydog.breed)
print (mydog.name)
print (Dog.species)
