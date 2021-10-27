#functions
def myname(x):
    print(x+" wolrd")
x="hello"
myname(x)

#forloop
numbers=[1,2,3,4,3,1,2,1,2]
for i in numbers:
    if(i==3):
        continue
    print(i)

for i in range(5,10):
    print(i)

#whileloop
i=5
a=[1,2,3,1,2,3,4,5]
while i in a:
    print("found")
    break