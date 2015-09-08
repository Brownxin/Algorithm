class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        res=[1 for i in range(1,n+1)]
        for i in range(2,n+1):
            res[i]=res[i-1]+res[i-2]
        return res[i]

