class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if len(nums)==0 or len(nums)==1:
            return nums
        for i in range(0,len(nums)):
            for j in range(0,len(nums)-1):
                if nums[j]>nums[j+1]:

                    t=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=t

        return nums

nums=[4, 5, 1, 2, 3]
so=Solution().recoverRotatedSortedArray(nums)
print(so)