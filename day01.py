import random
print(random.randrange(1,10))

x=" Born to rule " 
print(x.__len__())
print(len(x.strip()))

age=12
txt="I am {}"
print(type(txt.format(age)))

#Slicing
y="hello"
print(y[-3:-1])

# I want 5 mongos for 75 ruppees
a=5
b=75
text="I want {} mangos for {} ruppees"
print(text.format(a,b))

#To validate the datatype of a variable - use isinstance()
q="Hello \" World\""
print(q)

