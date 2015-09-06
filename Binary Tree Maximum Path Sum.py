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
    @return: An integer
    """
    maxpath=-(10 ** 10)
    def maxPathSum(self, root):
        # write your code here
        if root == None:
            return 0

        def findMaxPath(next):

            if next == None:
                return 0
            left_sum = findMaxPath(next.left)
            right_sum = findMaxPath(next.right)
            temp_max = next.val
            if left_sum > 0:
                temp_max += left_sum
            if right_sum > 0:
                temp_max += right_sum
            Solution.maxpath = max(Solution.maxpath, temp_max)

            return max(next.val, max(next.val + left_sum, next.val + right_sum))

        findMaxPath(root)
        return Solution.maxpath
