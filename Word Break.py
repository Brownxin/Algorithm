class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        # write your code here
        dp=[False for i in range(len(s)+1)]
        dp[0]=True
        for i in range(1,len(dp)):
            for j in range(i):
                if dp[j]==True and s[j:i] in dict:
                    dp[i]=True

        return dp[len(s)]

