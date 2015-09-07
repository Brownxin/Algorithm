"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = Solution(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""
class Solution:
    #@param root: The root of binary tree.
    def __init__(self, root):
        # write your code here
        self.cur=root
        self.stack=[]
    #@return: True if there has next node, or false
    def hasNext(self):
        # write your code here
        if self.stack==[] and self.cur==None:
            return False
        return True
    #@return: return next node
    def next(self):
        #write your code here
        while self.cur!=None:
            self.stack.append(self.cur)
            self.cur=self.cur.left

        self.cur=self.stack.pop()
        node=self.cur
        self.cur=node.right
        return node
