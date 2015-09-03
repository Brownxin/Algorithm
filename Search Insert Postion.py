class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if A==[]:
            return 0
        if A[len(A)-1]<target:
            index=len(A)
            return index
        for i in range(len(A)):
            if A[i]>=target:
                index=i
                return index



A=[]
target=9
so=Solution().searchInsert(A,target)
print(so)