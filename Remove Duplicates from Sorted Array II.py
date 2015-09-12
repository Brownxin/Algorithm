class Solution:
    # @param A a list of integers
    # @return an integer
    # @it's a good solution!
    def removeDuplicates(self, A):
        if len(A)<=2:
            return 2
        cur=2
        rep=1
        while cur<len(A):
            if A[cur]==A[rep] and A[cur]==A[rep-1]:
                cur+=1
            else:
                rep+=1
                A[rep]=A[cur]
                cur+=1
        return  rep+1

A=[1,1,1,2,2,3]
so=Solution().removeDuplicates(A)
print(so)
