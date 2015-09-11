class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        res=[1 for i in range(len(nums))]
        max=0
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<=nums[i]:
                    if res[i]<=res[j]+1:
                        res[i]=res[j]+1
                if res[i]>max:
                    max=res[i]

        return max