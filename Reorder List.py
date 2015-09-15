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
    @param head: The first node of the linked list.
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        if head==None or head.next==None or head.next.next==None:
            return None
        slow=fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        head1=head
        head2=slow.next
        slow.next=None

        dummy=ListNode(0)
        dummy.next=head2
        p=head2.next
        head2.next=None
        while p!=None:
            tmp=p
            p=p.next
            tmp.next=dummy.next
            dummy.next=tmp
        head2=dummy.next

        p1=head1
        p2=head2
        while p2!=None:
            tmp1=p1.next
            tmp2=p2.next
            p1.next=p2
            p2.next=tmp1
            p1=tmp1
            p2=tmp2
