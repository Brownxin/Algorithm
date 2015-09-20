class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        # write your code here
        result=[]
        def dfs(start,target,candiates,list):
            length=len(candidates)
            if target==0:
                result.append(list)
            for i in range(start,len(candidates)):
                if target<candidates[i]:
                    return 
                dfs(i,target-candidates[i],candidates,list+[candidates[i]])
        candidates.sort()
        dfs(0,target,candidates,[])
        return result