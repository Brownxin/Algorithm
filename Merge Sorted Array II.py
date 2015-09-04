class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        if A==None or A==[]:
            return B
        if B==None or B==[]:
            return A
        list=A+B
        list.sort()
        return list