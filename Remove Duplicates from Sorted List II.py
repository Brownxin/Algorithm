"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        dummy=ListNode(0)
        dummy.next=head
        cur=dummy
        tmp=dummy.next
        while cur.next!=None:
            while tmp.next!=None and tmp.next.val==cur.next.val:
                tmp=tmp.next
            if tmp==cur.next:
                tmp=tmp.next
                cur=cur.next
            else:
                cur.next=tmp.next

        return dummy.next