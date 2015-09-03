class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        temp=[]
        list=[]
        res=[]
        for i in range(len(A)-2):
            temp.append(A[i])
            temp.append(A[i+1])
            temp.append(A[i+2])
            list.append(temp)
            temp=[]

        for j in range(len(list)):
            temp_list=list[j]
            if (temp_list[1]>temp_list[0]) and (temp_list[1]>temp_list[2]):
                res.append(j+1)

        return res

nums=[1, 2, 1, 3, 4, 5, 7, 6]
so=Solution().findPeak(nums)
print(so)

