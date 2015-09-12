class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        j=0
        for i in range(len(A)):
            if A[i]!=A[j]:
                A[i],A[j+1]=A[j+1],A[i]
                j+=1

        return j+1