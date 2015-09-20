"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def merge(self,p1,p2):
        if p1 == None: return p2
        if p2 == None: return p1
        dummy=ListNode(0)
        p=dummy
        while p1!=None and p2!=None:
            if p1.val<=p2.val:
                p.next=p1
                p1=p1.next
                p=p.next
            else:
                p.next=p2
                p2=p2.next
                p=p.next
            if p1==None:
                p.next=p2
            if p2==None:
                p.next=p1
            return dummy.next


    def sortList(self, head):
        # write your code here
        if head==None or head.next==None:
            return head
        slow=fast=head
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        
        head1=head
        head2=slow.next
        slow.next=None
        
        head1=self.sortList(head1)
        head2=self.sortList(head2)
        return self.merge(head1,head2)