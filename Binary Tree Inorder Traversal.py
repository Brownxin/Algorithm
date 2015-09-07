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
    @return: Inorder in ArrayList which contains node values.
    """
    res=[]
    def inorderTraversal(self, root):
        # write your code here

        # write your code here
        if root==None:
            return []

        def postorderTraversal(next):
            if next==None:
                return
            postorderTraversal(next.left)
            Solution.res.append(next.val)
            postorderTraversal(next.right)


        postorderTraversal(root)
        return Solution.res