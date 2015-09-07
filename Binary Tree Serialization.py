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

    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    res=[]
    def serialize(self, root):
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


    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''
    def deserialize(self, data):
        # write your code here
        if data==[]:
            return None
        def constructTree(list,level,start):
            if level>len(list)-1:
                return
            root=TreeNode(list[level])
