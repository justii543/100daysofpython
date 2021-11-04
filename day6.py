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