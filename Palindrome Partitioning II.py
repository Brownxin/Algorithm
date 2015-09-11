class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        # write your code here
        dp=[0 for i in range(len(s)+1)]
        for i in range(len(dp)):
            dp[i]=len(s)-i

        p=[[False for i in range(len(s))] for j in range(len(s))]

        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if (s[i]==s[j]) and (((j-i)<2) or (p[i+1][j-1])):
                    p[i][j]=True
                    dp[i]=min(1+dp[j+1],dp[i])

        return dp[0]-1