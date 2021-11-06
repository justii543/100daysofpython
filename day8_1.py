from day8 import solve
A=[-10,90,34,-90]
B=2
class Solution:
    def solve(self, A, B):
            self.current_sum = sum(A[:B])
            self.max_sum = current_sum
            if B < len(A):
                for i in reversed(range(B)):
                    self.current_sum += -A[i] + A[i - B]
                    if current_sum > max_sum:
                        max_sum = current_sum
            return max_sum
p=solve(A,B)
print(p)