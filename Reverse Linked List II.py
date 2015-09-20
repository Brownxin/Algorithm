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
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        dummy=ListNode(0)
        dummy.next=head
        slow=fast=dummy
        length=n-m+1
        while length>0:
            fast=fast.next
            length-=1
        while m>1:
            slow=slow.next
            fast=fast.next
            m-=1
        head_end=fast.next
        p=slow.next
        per=fast.next
        while p!=fast:
            temp=p.next
            p.next=per
            per=p
            fast.next=p
            p=temp
            slow.next=p
        return dummy.next
