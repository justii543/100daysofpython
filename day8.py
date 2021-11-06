#prgm to find greatest sum of elements from both sides
A=[-1,39,2,33,5,6,-9,34]
B=3
def solve(A,B):
    current_sum=sum(A[:B])
    max_val=0
    if B<len(A):
        for i in range(B):
            max_val+=A[len(A)-1-i]
    imax=max(current_sum,max_val)
    print(imax)
solve(A,B)



# for i in reversed(range(10)):
#     print(i)


#self Keyword - reference of class
#if you create say two methods in a class and try to call one inside another, 
# it does not recognize method unless you add "self"--reference of class
class foo:
    def sample(self,num1,num2):
        self.n1=num1
        self.n2=num2
    def add(self):
        return self.n1+self.n2


#del keyword
A=[1,2,3,4,5,6,7,8]
del A[2]  #o/p--[1,2,4,5,6,7,8]


#zip function - returns as tuple

A=["justi","ram","joseph"]
B=["kurian","cv","mj"]
p=zip(A,B)
print(tuple(p))