class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        # write your code here
        def getMid(list):
            sum=0
            if len(list)%2==0:
                sum=list[int(len(list)/2)]+list[int(len(list)/2-1)]
                mid=sum/2
            else:
                mid=list[int((len(list)-1)/2)]
            return mid

        def getIndex(list,target):
            mid=getMid(list)
            if mid>=target:
                for i in range(int(len(list)/2)+1):
                    if list[i]==target:
                        return i
            else:
                for i in range(int(len(list)/2)-1,len(list)):
                    if list[i]==target:
                        return i

            return -1

        index=0
        index=getIndex(nums,target)
        return index


nums=[2,6,7]
target=3
So=Solution().binarySearch(nums,target)
print(So)