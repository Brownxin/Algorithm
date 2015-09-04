class Solution:
    """
    @param A : an integer ratated sorted array and duplicates are allowed
    @param target : an integer to be searched
    @return : a boolean
    """
    def findMin(self, num):
        # write your code here
        if num==[] or num==None:
            return num

        def findElement(list,min):
            if len(list)==1:
                if list[0]<min:
                    min=list[0]
                return min

            mid=int(len(list)/2)
            left=list[:mid]
            right=list[mid:]
            min=findElement(left,min)
            min=findElement(right,min)
            return min

        min=findElement(num,num[0])
        return min
