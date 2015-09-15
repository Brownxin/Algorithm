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

import heapq
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        heap=[]
        for node in lists:
            if node!=None:
                heap.append((node.val,node))
        heapq.heapify(heap)
        head=ListNode(0)
        cur=head
        while heap!=[]:
            pop=heapq.heappop(heap)
            cur.next=ListNode(pop[0])
            cur=cur.next
            if pop[1].next!=None:
                heapq.heappush(heap,(pop[1].next.val,pop[1].next))
        return head.next