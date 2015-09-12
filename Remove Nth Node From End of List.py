"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        dummy=ListNode(0)
        dummy.next=head
        p1=p2=dummy
        for i in range(n):
            p1=p1.next
        while p1.next!=None:
            p1=p1.next
            p2=p2.next
        p2.next=p2.next.next
        return dummy.next