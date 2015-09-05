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
        if root==None:
            return True
        def isValid(next):
            if next==None:
                return True
            if not next.left==None:
                if next.left.val>=next.val:
                    return False
            if not next.right==None:
                if next.right.val<=next.val:
                    return False
            flag=isValid(next.left)
            flag=flag and isValid(next.right)
            return flag

        flag=isValid(root)
        return flag

