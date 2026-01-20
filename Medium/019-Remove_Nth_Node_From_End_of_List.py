# 19. Remove Nth Node From End of List
# Given the head of a linked list,
# remove the nth node from the end of the list and return its head.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        slow = head
        fast = head

        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next

        # If fast is None, delete the head
        if fast is None:
            return head.next

        # Move both pointers until fast reaches last node
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        # Delete the nth node from the end
        slow.next = slow.next.next
        return head


# -------- Testing --------

# Creating linked list: 1 → 2 → 3 → 4 → 5 → 6
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

n = 2  # remove 2nd node from end (node with value 5)

sol = Solution()
new_head = sol.removeNthFromEnd(head, n)

# Display updated linked list
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")
