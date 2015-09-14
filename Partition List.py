"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class ListNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
class Solution:
    """
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode 
    """
    def partition(self, head, x):
        # write your code here
        head1=ListNode(0)
        head2=ListNode(0)
        cur=head
        phead1=head1
        phead2=head2
        while cur!=None:
            if cur.val<x:
                phead1.next=cur
                cur=cur.next
                phead1=phead1.next
                phead1.next=None
            else:
                phead2.next=cur
                cur=cur.next
                phead2=phead2.next
                phead2.next=None
        phead1.next=head2.next
        head=head1.next
        return head