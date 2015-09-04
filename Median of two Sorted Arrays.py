class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here


        def getMid(list):
            sum=0
            if len(list)%2==0:
                sum=float(list[int((len(list)/2))]+list[int((len(list)/2-1))])
                mid=sum/2
            else:
                mid=float(list[(len(list)-1)/2])
            return mid

        if A==[] and B==[]:
            return []
        elif A==None and B==None:
            return None
        elif A==[] or A==None:
            return getMid(B)
        elif B==[] or B==None:
            return getMid(A)

        C=A+B
        C.sort()
        Mid=getMid(C)
        return Mid

A=[1,2,3,4,5,6]
B=[2,3,4,5]

so=Solution().findMedianSortedArrays(A,B)
print(so)

