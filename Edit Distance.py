class Solution: 
    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    def minDistance(self, word1, word2):
        # write your code here
        dp=[[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]

        for j in range(len(dp[0])):
            dp[0][j]=j

        for i in range(len(dp)):
            dp[i][0]=i

        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                dp[i][j]=min(1+dp[i-1][j],1+dp[i][j-1],dp[i-1][j-1]+(0 if word1[i-1]==word2[j-1] else 1))

        return dp[len(dp)-1][len(dp[0])-1]