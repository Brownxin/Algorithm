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
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        # write your code here
        if root==None:
            return True
        def getHight(next):
            if next==None:
                return 0
            left_depth=getHight(next.left)
            right_depth=getHight(next.right)
            if left_depth>0:
                left_depth+=1
            if right_depth>0:
                right_depth+=1
            return max(1,max(left_depth,right_depth))

        left_depth=getHight(root.left)
        right_depth=getHight(root.right)

        if (left_depth-right_depth)**2>1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

