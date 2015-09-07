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
    @return: buttom-up level order in a list of lists of integers
    """
    res=[]
    def levelOrderBottom(self, root):
        # write your code here
        if root==None:
            return []

        def LevelOrder(next,level):
            if next==None:
                return
            if len(Solution.res)<level+1:
                Solution.res.insert(0,[])

            Solution.res[len(Solution.res)-1-level].append(next.val)


            LevelOrder(next.left,level+1)
            LevelOrder(next.right,level+1)

        LevelOrder(root,0)

        return Solution.res