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
    @return: Level order in a list of lists of integers
    """
    res=[]
    def levelOrder(self, root):
        # write your code here
        if root==None:
            return []

        def levelTraversal(next,level):
            if next==None:
                return
            if len(Solution.res)<level+1:
                Solution.res.append([])
            Solution.res[level].append(next.val)

            levelTraversal(next.left,level+1)
            levelTraversal(next.right,level+1)

        levelTraversal(root,0)
        return Solution.res