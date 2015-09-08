class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        # write your code here
        jumpNum=0
        maxArrived=0
        maxReach=0
        for i in range(len(A)):
            if i>maxArrived:
                jumpNum+=1
                maxArrived= maxReach
            maxReach=max(i+A[i],maxReach)
        return jumpNum