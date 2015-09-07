"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """
    res=[]
    def searchRange(self, root, k1, k2):
        # write your code here
        if root==None:
            return []

        def getList(next):
            if next==None:
                return
            

            getList(next.left)
            if next.val>=k1 and next.val<=k2:
                Solution.res.append(next.val)
            getList(next.right)

        getList(root)
 
        return Solution.res