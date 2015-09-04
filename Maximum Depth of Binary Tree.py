"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    class TreeNode():
        def __init__(self,val):
            self.val=val
            self.left,self.right=None,None


    def maxDepth(self, root):
        # write your code here
        if root==None:
            return 0

        leftDepth=self.maxDepth(root.left)
        rightDepth=self.maxDepth(root.right)

        if leftDepth>rightDepth:
            return leftDepth+1
        if rightDepth>=leftDepth:
            return rightDepth+1


