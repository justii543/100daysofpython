list=['bus','car','bike']
def loop(x):
    print(x*3)
loop(list)
#modified
def loopin(crazy,list):
    for i in list:
        crazy(i)
loopin(loop,list)

#list,tuple,dictionary,set
#list-can have diff. data types.| ordered, changeable,allow duplicates.
list=['car','bike',10,2.3,True]
print(list)
print(len(list))
print(type(list))
print(list[0])
print(list[2:4])  #range
list.insert(2,"home")  #insert at any position
print(list)
list.append("bus")
print(list)


 