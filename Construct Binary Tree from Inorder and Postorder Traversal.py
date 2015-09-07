"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    """
    @param inorder : A list of integers that inorder traversal of a tree
    @param postorder : A list of integers that postorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, inorder, postorder):
        # write your code here
        if inorder==[]:
            return None
        root=TreeNode(postorder[len(postorder)-1])
        root_inorder_index=inorder.index(postorder[len(postorder)-1])
        root.right=self.buildTree(inorder[root_inorder_index+1:],postorder[root_inorder_index:len(postorder)-1])
        root.left=self.buildTree(inorder[:root_inorder_index],postorder[:root_inorder_index])

        return root