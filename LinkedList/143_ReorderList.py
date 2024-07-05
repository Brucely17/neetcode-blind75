# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        size=0
        temp=head
        
        while temp:
            size+=1
            temp=temp.next
        seperation=size//2
        remainingSize=size-seperation
        
        list1=head
        dummy=head
        temp=list1
        while remainingSize>0:
            dummy=dummy.next
            remainingSize-=1
            if remainingSize==0:
                print(temp)
                temp.next=None
            temp=temp.next
            
        list2=dummy
        
        list2=self.reverseList(list2)

        # temp1=list1
        # temp2=list2
        curr=ListNode()
        while list1 and list2:
            next1=list1.next
            next2=list2.next
            curr.next=list1
            curr.next.next=list2
            curr=curr.next.next
            list1=next1
            list2=next2
        if list1:
            curr.next=list1
        elif list2:
            curr.next=list2
        # print("\n",curr)

            


        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        temp=head
        while temp:
            sub=temp.next
            temp.next=prev
            prev=temp
            temp=sub
            # print(temp.val,head.val)
        
        return prev