# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) :

        temp=head
        visit=set()
        # visit.add(temp.val)
        while temp:
            if temp in visit:
                return True
            
            
            visit.add(temp)
            temp=temp.next
            # print(temp.val)
            # print('t:',temp.val)
        return False

s=Solution()
head=ListNode(3)
head.next=ListNode(2)
head.next.next=ListNode(0)
head.next.next.next=ListNode(-4)
print(s.hasCycle(head))