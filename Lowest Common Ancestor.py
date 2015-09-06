"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import copy
class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """ 
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if root==None:
            return None
        def getPath(next):
            if next==None:
                return None
            if next==A or next==B:
                return next
            left=getPath(next.left)
            right=getPath(next.right)

            if left!=None and right!=None:
                return next

            if left==None:
                return right
            return left

        node=getPath(root)
        return node
