class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        if A==[] or A==None:
            return 0
        res=[]
        list=set(A)
        temp=[i for i in list]
        index=[]
        for i in range(len(temp)):
            count=0
            for j in range(len(A)):
                if A[j]==temp[i] and count<1:
                    count+=1
                    index.append(j)
                    break
        temp_list=[]
        for i in range(len(A)):
            if not i in index:
                temp_list.append(A[i])
        temp_2=[i for i in set(temp_list)]
        temp=temp+temp_2

        temp.sort()
        length=len(temp)
        return length,temp


A=[-14,-14,-14,-14,-14,-14,-14,-13,-13,-13,-13,-12,-11,-11,-11,-9,-9,-9,-7,-7,-7,-6,-6,-5,-5,-5,-4,-4,-4,-3,-3,-3,-2,-2,-2,-1,-1,0,0,0,0,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,5,5,6,6,6,7,7,7,7,8,8,8,8,9,9,10,10,11,11,11,11,11,12,12,12,12,13,13,13,13,14,14,15,16,17,18,18,18,20,20,21,21,21,21,21,22,22,22,22,23,24,24,25]

so=Solution().removeDuplicates(A)
print(so)
