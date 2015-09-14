"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """
    def get_list(self,sorted_list):
        length=len(sorted_list)
        if length<1:
            return None
        if length<2:
            return TreeNode(sorted_list[0])
        root=TreeNode(int(sorted_list[length/2]))
        root.left=self.get_list(sorted_list[:int(length/2)])
        root.right=self.get_list(sorted_list[int(length/2)+1:])
        return root

    def sortedListToBST(self, head):
        # write your code here
        p=head
        res_list=[]
        while p!=None:
            res_list.append(p.val)
            p=p.next
        return self.get_list(res_list)

