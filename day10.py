#OBJECTS AND CLASSES
 # __init__ --This method called when an object is created from the class 
 # and it allow the class  to initialize the attributes of a class.
from typing import List


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


#lambda function - diff. arguments can be passed but only one expression 
# can be evaluated.
x=lambda a,b: a+2*b
print(x(3,4))

#lambda within another function
def f1(n):
    return lambda a:a+n
x=f1(5)  #5 is passed as argument to f1
y=f1(8)
print(x(2))  #2 is passed as argument to lambda funcn within f1
print(y(4))

#FILTER FUNCTION
#it filters an array based on boolean array

def prime(x):
    for i in range(2,x):  
        if x%2==0:
            return False
        else:
            return True  
filtered=filter(prime,range(10))  #syntax==> filter(function (which perform test),sequence(list,tuple,..)) 
                                             #filter function takes the true value only
print("prime numbers are:  ", list(filtered ))

#MAP FUNCTION
def square(n):
    return n*n
numbers=[1,2,3,4,5]
mapped=map(square,numbers)  #syntax==> map(function,input values)
print(list(mapped))