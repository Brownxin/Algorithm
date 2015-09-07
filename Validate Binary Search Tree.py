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
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        # write your code here
        if root == None:
            return True

        def isValid(next,min,max):
            if next==None:
                return True
            if next.val<=min or next.val>=max:
                return False
            return isValid(next.left,min,next.val) and isValid(next.right,next.val,max)

        return isValid(root,-10**10,10**10)
