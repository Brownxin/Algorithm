class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        flag=True
        Reach=A[0]

        for i in range(len(A)-1):
            if Reach>0:
                Reach-=1
                Reach=max(A[i],Reach)
            else:
                flag=False
        return flag