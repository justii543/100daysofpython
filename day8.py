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
