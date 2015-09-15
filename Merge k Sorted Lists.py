"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def get_index(self,num,low,high):
        tmp=num[low]
        while low<high:
            while low<high and tmp<num[high]:
                high-=1
            if low<high:
                num[low]=num[high]
                low=+1
            while low<high and tmp>num[low]:
                low+=1
            if low<high:
                num[high]=num[low]
                high-=1
        num[low]=tmp
        return low
    def quicksort(self,num,low,high):
        if low<high:
            index=self.get_index(num,low,high)
            self.quicksort(num,low,index-1)
            self.quicksort(num,index+1,high)
        return num
    def mergeKLists(self, lists):
        # write your code here
        if lists==[]:
            return None
        res=[]
        count=0
        for k in lists:
            if k==None:
                count+=1
            while k!=None:
                res.append(k.val)
                k=k.next
        if count==len(lists):
            return None
        res=self.quicksort(res,0,len(res)-1)
        # print res
        head=ListNode(res[0])
        p=head
        for i in range(1,len(res)):
            p.next=ListNode(res[i])
            p=p.next
        p.next=None
        return head

