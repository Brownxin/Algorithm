class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if not len(s1)+len(s2)==len(s3):
            return False

        dp=[[False for j in range(len(s2)+1)] for i in range(len(s1)+1)]
        m=len(dp)
        n=len(dp[0])
        dp[0][0]=True
        for i in range(1,len(dp)):
            dp[i][0]=dp[i-1][0] and (s1[i-1]==s3[i-1])
        for i in range(1,len(dp[0])):
            dp[0][i]=dp[0][i-1] and (s2[i-1]==s3[i-1])

        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                flag_s1=dp[i-1][j] and (s1[i-1]==s3[i+j-1])
                flag_s2=dp[i][j-1] and (s2[j-1]==s3[i+j-1])
                dp[i][j]=flag_s1 or flag_s2

        return dp[m-1][n-1]