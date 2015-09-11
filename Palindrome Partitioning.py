class Solution:
    # @param s, a string
    # @return a list of lists of string
    res=[]
    def partition(self, s):
        # write your code here
        def isPalindrome(self, s):
            for i in range(len(s)):
                if s[i] != s[len(s)-1-i]: return False
            return True
        def dfs(s,list):
            if len(s)==0:
                Solution.res.append(list)
                return
            for i in range(1,len(s)+1):
                if isPalindrome(s[:i]):
                    dfs(s[i:],list+[s[:i]])

        dfs(s,[])
        return Solution.res