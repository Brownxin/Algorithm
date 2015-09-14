class ListNode():
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
class rever():
    def __init__(self,head):
        self.head=head

    def rever_linklist(self):
        pre=ListNode(0)
        next=self.head.next
        while self.head.next!=None:
            nex=self.head.next
            self.head.next=pre
            pre=self.head
            self.head=nex

        self.head.next=pre
        return self.head