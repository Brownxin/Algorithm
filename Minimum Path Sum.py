class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        m=len(grid)
        n=len(grid[0])

        dp=[[0 for i in range(n)] for i in range(m)]
        dp[0][0]=grid[0][0]

        for i in range(1,m):
            dp[i][0]=grid[i][0]+dp[i-1][0]
        for i in range(1,n):
            dp[0][i]=grid[0][i]+dp[0][i-1]

        for i in range(1,m):
            for j in range(1,n):
               dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[m-1][n-1]
