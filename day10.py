#OBJECTS AND CLASSES
 # __init__ --This method called when an object is created from the class 
 # and it allow the class  to initialize the attributes of a class.
class Human:
    def __init__(self,name ,age):   #self is used to access variables belong to class
         self.name=name
         self.age=age
    def methods(self):
        print("lets begin by "+ self.name)
h1= Human("justi",22)
h2=Human("jeez",24)
h1.methods()


#to modify elemnets

h1.name="kurian"
h1.age=60
h1.methods()
h2.methods()
print(h1.name)

#deleting a object
# del h2
# h2.methods()

#empty class
class Emp:
    pass
