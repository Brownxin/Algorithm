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
    @return: A list of list of integer include 
             the zig zag level order traversal of its nodes' values
    """
    res=[]
    def zigzagLevelOrder(self, root):
        # write your code here
        if root==None:
            return []

        def LevelOrder(next,level):
            if next==None:
                return
            if len(Solution.res)<level+1:
                Solution.res.append([])
            if level%2==0:
                Solution.res[level].append(next.val)
            else:
                Solution.res[level].insert(0,next.val)

            LevelOrder(next.left,level+1)
            LevelOrder(next.right,level+1)

        LevelOrder(root,0)

        return Solution.res