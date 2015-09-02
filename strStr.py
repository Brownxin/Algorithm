class Solution:
    def strStr(self, source, target):
        # write your code here
        self.source=source
        self.target=target
        if target=="":
            return 0
        if source=="" or source==None or target==None:
            return -1
        length = len(target)-1
        for i in range(0,len(source)):
            if i+length>=len(source):
                break
            s=''
            for c in range(i,i+length+1):
                s=s+source[c]
            if s==target:
                return 1
        return -1

source=None
target='a'

So=Solution()
print(So.strStr(source,target))

