class Solution: 
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        # write your code here
        m=len(S)+1
        n=len(T)+1
        dp=[[0 for i in range(n)] for i in range(m)]
        for i in range(m):
            dp[i][0]=1
        
        for i in range(1,m):
            for j in range(1,n):
                if S[i-1]==T[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        
        return dp[m-1][n-1]
