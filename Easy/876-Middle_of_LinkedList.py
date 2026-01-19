# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.


from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast != None and fast.next!= None:
            slow = slow.next
            fast= fast.next.next
            
        return slow
   
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

sol = Solution()
mid = sol.middleNode(head)
print(mid.val)