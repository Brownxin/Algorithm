class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        sPointer=pPointer=sStar=0
        pStar=-1
        count=0
        while sPointer<len(s):
            if pPointer<len(p) and (s[sPointer]==p[pPointer] or p[pPointer]=='?'):
                sPointer+=1
                pPointer+=1
                continue
            if pPointer<len(p) and p[pPointer]=='*':
                pStar=pPointer
                sStar=sPointer
                pPointer+=1
                continue
            if pStar!=-1:
                pPointer=pStar+1
                sStar+=1
                sPointer=sStar
                continue
            return False

        while pPointer<len(p) and p[pPointer]=='*':
            pPointer+=1
        if pPointer==len(p):
            return True
        return False
s="abcdefg"
p="?b*fg"
so=Solution().isMatch(s,p)
print(so)
