class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        # write your code here
        def permute(temp,temp_list):
            if len(temp)==0:
                if not temp_list in result:
                    result.append(temp_list)
            for i in range(0, len(temp)):
                next_temp_list=temp_list[:]
                next_temp=temp[:]
                next_temp_list=next_temp_list+[temp[i]]
                next_temp.pop(i)
                permute(next_temp,next_temp_list)

        if nums==None:
            return []
        if len(nums)==0:
            return []
        if nums=='Null':
            return []

        result=[]
        list=[]
        permute(nums,list)
        return result


nums=None

Solu=Solution().permuteUnique(nums)
print(Solu)