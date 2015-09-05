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
    @return: Preorder in ArrayList which contains node values.
    """
    class TreeNode():
        def __init__(self,val):
            self.val=val
            self.left,self.right=None,None



    def preorderTraversal(self, root):
        # write your code here
        if root==None:
            return []
        res=[]
        def preorder(next):
            if next==None:
                return
            res.append(next.val)
            preorder(next.left)
            preorder(next.right)

        preorder(root)
        return res

A={1,2,3}
so=Solution().preorderTraversal(A)





