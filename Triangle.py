class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        # write your code here
        if len(triangle)==0:
            return 0
        res=[0 for i in range(len(triangle))]
        res[0]=triangle[0][0]

        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])-1,-1,-1):
                if j==len(triangle[i])-1:
                    res[j]=res[j-1]+triangle[i][j]
                elif j==0:
                    res[j]=res[j]+triangle[i][0]
                else:
                    res[j]=min(res[j],res[j-1])+triangle[i][j]

        return min(res)