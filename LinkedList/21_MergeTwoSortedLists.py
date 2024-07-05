class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2) :
        dummy=ListNode()
        curr=dummy

        while list1 and list2:

            if list1.val<=list2.val:
                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next
            curr=curr.next
        
        if list1:
            curr.next=list1
        elif list2:
            curr.next=list2




        return dummy.next


s=Solution()
l1=ListNode(1,ListNode(2,ListNode(4)))
l2=ListNode(1,ListNode(3,ListNode(4)))
# print(s.mergeTwoLists(l1,l2))

node=s.mergeTwoLists(l1,l2)

while node:
    print(node.val)
    node=node.next

