class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubsequence(self, A, B):
        dp=[[0 for i in range(len(B)+1)] for j in range(len(A)+1)]
        
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                if A[i-1]==B[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
    
        return dp[len(dp)-1][len(dp[0])-1]