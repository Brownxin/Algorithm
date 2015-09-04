class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        self.A=A
        if A==[] or A==None:
            return A
        list=[i for i in set(A)]
        list.sort()
        return list

A = [1,1,2,2,7,7,8,9,9,10,12,12,14]
so=Solution().removeDuplicates(A)
print(so)