class Solution:
    """
    @param A : an integer ratated sorted array and duplicates are allowed
    @param target : an integer to be searched
    @return : a boolean
    """
    def search(self, A, target):
        # write your code here
        if A==[] or A==None:
            return False
        flag=False
        def findElement(list,flag):
            if flag:
                return True
            if len(list)==1:
                if list[0]==target:
                    return True
                return flag

            mid=int(len(list)/2)
            left=list[:mid]
            right=list[mid:]
            flag=findElement(left,flag)
            flag=findElement(right,flag)
            return flag

        flag=findElement(A,flag)
        return flag

so=Solution().search([10001,10001,10007,1,10,1001,2001], 10001)
print(so)
