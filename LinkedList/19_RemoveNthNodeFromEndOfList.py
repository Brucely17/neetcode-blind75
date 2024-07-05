# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size=0
        temp=head
        
        while temp:
            size+=1
            temp=temp.next
        

        if size==1:
            return 
        
        removeElement=size-n
        
        if removeElement==0:
            return head.next

        prev=ListNode()
        curr=head
        i=0
        while curr:
            
            
            if i==removeElement:

                newNext=curr.next
                prev.next=newNext
                break

            prev=curr
            curr=curr.next
            i+=1
            
        