#tuple-ordered,UNCHANGEABLE,and allow duplicates.
a=("justin",22,3.0,"begin",True)
print(tuple)
print(len(a))
print(tuple[2])

#single elemnt
q=("jsutii",) # without ',' it is of type string
print(q)

#append is applicable in tuple but tuple can be altered using type conversion method
y=list(a)
y.append("lambo")
x=tuple(y)
print(x)

#Dictionary
#unordered, changeable, NO Duplicates.- it overwrites the exsisting value
dicti={"name": "Justin",
    "age":22,
    "DOB":"11/5/99",
    "cars":"lambo"
}
print(dicti)
print(len(dicti))

#changing the value of a key
dicti["cars"]="Gwagon"
print(dicti)

#update
dicti.update({"age":24})
print(dicti)

#deleting a key
dicti.pop("DOB")
print(dicti)

#for loop
fruits=["apple","banana","strawberry","kiwi"]
favfruits=[]
for i in fruits:
    if "a" in i:
        favfruits.append(i)
print(favfruits)

#list comprehension= to compress to code into single line

newfruit=[j for j in fruits if "a" in j]
print(newfruit)

#range
newlist=[i for i in range(10)]
print(newlist)

#upper case
nw=[j.upper() for j in fruits]
print(nw) 