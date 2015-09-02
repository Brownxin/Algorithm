class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        # write your code here
        def dfs(depth,start,list):
            if not list in result:
                result.append(list)
            if depth==len(S):
                return
            for i in range(start,len(S)):

                dfs(depth+1,start+1,(list+[S[i]]))
                depth+=1
                start+=1

        result=[]
        S.sort()
        dfs(0,0,[])
        return result

S=[0]
Re=Solution().subsetsWithDup(S)
print(Re)

