#random Number generation

import random
r=random.randint(1,100)
print(r)
print(type(r))

#isdigit method -string input
a="101"
print(a.isdigit())


# #concatenation is only possible b/w two strings
# ans=input("What is "+ 22)  #wrong

#CLASS & OBHECTS
#Properties of objects are methods
class Humam:
    x=5
h1=Humam()
print(h1.x)
print(Humam.x)

