# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if head==None:
            return None
        p=head
        while p!=None:
            NewNode=RandomListNode(p.label)
            NewNode.next=p.next
            p.next=NewNode
            p=p.next.next

        p=head
        while p!=None:
            if p.random!=None:
                p.next.random=p.random.next
            p=p.next.next

        new_head=head.next
        p_old=head
        p_new=new_head

        while p_new!=0:
            p_old.next=p_new.next
            p_old=p_old.next
            p_new.next=p_old.next
            p_new=p_new.next
        p_new.next=None
        p_old.next=None

        return new_head


