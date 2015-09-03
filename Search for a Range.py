class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
     # write your code here

            def getIndex(list,target):
                temp_index=[-1,-1]
                mid=int(len(list)/2)
                if mid>target:
                    for i in range(mid+1):
                        if list[i]==target:
                            temp_index[0]=i
                            break
                    for i in range(mid,-1,-1):
                        if list[i]==target:
                            temp_index[1]=i
                            break
                else:
                    for i in range(mid+1,len(list)):
                        if list[i]==target:
                            temp_index[0]=i
                            break
                    for i in range(len(list)-1,mid,-1):
                        if list[i]==target:
                            temp_index[1]=i
                            break

                return temp_index

            if A==[] or A==None:
                return [-1,-1]
            if len(A)==1:
                return [0,0]
            index=getIndex(A,target)
            return index

A=[9,10,100,101,1002,10203]
target=10203
so=Solution().searchRange(A,target)
print(so)
