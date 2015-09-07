class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """ 
    def uniquePaths(self, m, n):
        # write your code here
        grid=[[0 for i in range(n)] for j in range(m)]
        grid[0]=[1 for i in range(n)]
        for i in range(m):
            grid[i][0]=1
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j]=grid[i-1][j]+grid[i][j-1]

        return grid[m-1][n-1]