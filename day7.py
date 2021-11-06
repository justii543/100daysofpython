#file handling
from os import write


f=open("sample.txt","r")

# print(f.read())  --prints entire file
print(f.readline()) #prints one line 
print(f.readline(5))  # prints upto 5th element of 2nd line


for i in f:
    print(i)  # prints the file

f.close()

f=open("sample.txt","w")  #a refers to append--adds line to the file
f.write("WElcome back !")
f.close()

f.open("sample.txt","r")
print(f.read())