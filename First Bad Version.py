#class VersionControl:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use VersionControl.isBadVersion(10) to check whether version 10 is a
# bad version.
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use VersionContro



class Solution:
    """
    @param n: An integers.
    @return: An integer which is the first bad version.
    """

    def findFirstBadVersion(self, n):
        # write your code here
        start=1
        end=n
        while start+1<end:
            mid=int((end+start)/2)
            if VersionControl.isBadVersion(mid):
                end=mid
            else:
                start=mid
        if VersionControl.isBadVersion(start):
            return start
        elif VersionControl.isBadVersion(end):
            return end