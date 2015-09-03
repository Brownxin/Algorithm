class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        index=-1
        if A==[] or A==None:
            return index

        for i in range(len(A)):
            if target==A[i]:
                index=i
                return index

        return index